# module defines an application to curate a playlist
# with a sqlite3 db as a backend for data storage

from helper import helper
from db_operations import db_operations
from os.path import exists

data = helper.data_cleaner("songs.csv")

# modify to your chinook db connection
db_ops = db_operations("C:\\Users\\tfail\\Desktop\\Coding\\chinook.db")

# function checks if the table is empty or not
def is_empty():
    query = "SELECT COUNT(*) FROM songs;"
    result = db_ops.single_record(query)
    return result == 0

# function inserts data into table if it is empty
def pre_process():
    if is_empty():
        attribute_count = len(data[0])
        placeholders = ("?,"*attribute_count)[:-1]
        query = "INSERT INTO songs VALUES("+placeholders+")"
        db_ops.bulk_insert(query,data)
    # Prompt User to load in new songs
    loadNewSongs()

def loadNewSongs():
    # Prompt User to load new songs
    print("Would you like to load new songs?")
    print("This function will remove any records with songsIds that already exist.")
    print("Enter 1 for yes or 2 for no")
    num = helper.get_choice([1,2])
    if num == 1:
        # Ensure the file entered from user exits then retrieve data
        pathExists = False
        while pathExists == False:
            userPath = input("Enter location of file to be added: ")
            pathExists = exists(userPath)
            if (pathExists == False):
                print("File not found try again")
        userData = helper.data_cleaner(userPath)
        attribute_count = len(userData[0])
        placeholders = ("?,"*attribute_count)[:-1]         

        # BONUS: Preform check to see if ID already exists
        # If id exits remove it from the array
        existsQuery = "SELECT songId FROM songs;"
        keysList = db_ops.wholeRecord(existsQuery)
        inNumRecords = len(userData)
        tempList = []
        counter = 0
        for record in userData:         # get index of keys that are identical
            for key in keysList:
                if key[0] == record[0]:
                    tempList.append(counter)
            counter = counter + 1
                    
        tempList.reverse()            
        for x in tempList:              # remove all records w/ identical ids
            userData.remove(userData[x])      

        numRecords = len(userData)
        difRecords = inNumRecords - numRecords
        print(f"Removed {difRecords} records from query...")
        print(f"Insterting {numRecords} records into database...")                  
 
        # insert recrods into database
        query = "INSERT INTO songs VALUES("+placeholders+")"        
        db_ops.bulk_insert(query,userData)

def start_screen():
    print("Welcome to your playlist!")

# show user options
def options():
    print("Select from the following menu options:\n1 Find songs by artist\n" \
    "2 Find songs by genre\n3 Find songs by feature\n4 Update record information \n" \
    "5 Delete song from table\n6 Delete all songs with a null value\n7 Exit")
    return helper.get_choice([1,2,3,4,5,6,7])

# option 1, search table to show songs by artist
def search_by_artist():
    query = '''
    SELECT DISTINCT Artist
    FROM songs;
    '''
    print("Artists in playlist:")
    artists = db_ops.single_attribute(query)

    # show artists in table, also create dictionary for choices
    choices = {}
    for i in range(len(artists)):
        print(i,artists[i])
        choices[i] = artists[i]
    index = helper.get_choice(choices.keys())

    # user can ask to see 1, 5, or all songs
    print("How many songs do you want returned for",choices[index]+"?")
    print("Enter 1, 5, or 0 for all songs")
    num = helper.get_choice([1,5,0])

    # prepare query and show results
    query = "SELECT DISTINCT name FROM songs WHERE Artist=:artist ORDER BY RANDOM()"
    dictionary = {"artist":choices[index]}
    if num != 0:
        query +=" LIMIT:lim"
        dictionary["lim"] = num
    helper.pretty_print(db_ops.name_placeholder_query(query,dictionary))


# option 2, search table for songs by genre
def search_by_genre():
    query = '''
    SELECT DISTINCT Genre
    FROM songs;
    '''
    print("Genres in playlist:")
    genres = db_ops.single_attribute(query)

    # show genres in table, also create dictionary for choices
    choices = {}
    for i in range(len(genres)):
        print(i,genres[i])
        choices[i] = genres[i]
    index = helper.get_choice(choices.keys())

    # how many records
    print("How many songs do you want returned for",choices[index]+"?")
    print("Enter 1, 5, or 0 for all songs")
    num = helper.get_choice([1,5,0])

    # run query and show results
    query = "SELECT DISTINCT name FROM songs WHERE Genre =:genre ORDER BY RANDOM()"
    dictionary = {"genre":choices[index]}
    if num != 0:
        query +=" LIMIT:lim"
        dictionary["lim"] = num
    helper.pretty_print(db_ops.name_placeholder_query(query,dictionary))

# option 3, search songs by asc,desc order of audio feature
def search_by_feature():
    features = ['Danceability','Liveness','Loudness'] # features to show the user
    choices = {}
    for i in range(len(features)):
        print(i,features[i])
        choices[i] = features[i]
    index = helper.get_choice(choices.keys())

    # how many records
    print("How many songs do you want returned for "+choices[index]+"?")
    print("Enter 1, 5, or 0 for all songs")
    num = helper.get_choice([1,5,0])

    # order  by ascending or descending
    print("Do you want results sorted by the feature in ascending or descending order?")
    order = input("ASC or DESC: ")

    # prepare query and show results
    query = "SELECT DISTINCT Name FROM songs ORDER BY "+choices[index]+" "+order
    dictionary = {}
    if num!=0:
        query+=" LIMIT :lim"
        dictionary['lim'] = num
    helper.pretty_print(db_ops.name_placeholder_query(query,dictionary))

def updateInformation():
    # Get song to be updated from user
    songName = input("Enter name of song you wish to update: ")
    query = "SELECT * FROM songs WHERE Name = :val1;"
    tempDict = {"val1":songName}
    print()
    songData = db_ops.wholeRecordDictionary(query, tempDict)
    if len(songData) == 0:
        print("Song not found...")
        return

    # Data Cleanup + Printing data to user
    songData = songData[0]
    songDataChoices = [songData[1], songData[2], songData[3], songData[4], songData[6]]
    helper.songsPrint(songData)
    print("")
   
    # Print all the values for the given song and allow user to choose which to change
    print("Select an option for wich value you wish to change:")
    print("0 - Song Name, 1 - Artist, 2 - Album, 3 - Release Date, 4 - Explicit")
    choices = {}
    for i in range(len(songDataChoices)):
        print(i,songDataChoices[i])
        choices[i] = songDataChoices[i]
    index = helper.get_choice(choices.keys())

    # Ensuring correct input is entered
    userUpdate = None
    if index == 4:
        while userUpdate != 'T' and userUpdate != 'F':
            userUpdate = input("Enter T to change to True, F to change to False: ")
        if userUpdate == 'T':
            userUpdate = "True"
        else:
            userUpdate = "False"
    elif index == 3:
        while True:
            print("Date format should be YYYY/MM/DD")
            userUpdate = input("Enter a date: ")
            if len(userUpdate) == 10 and helper.containsNumber(userUpdate):
                break
    else:
        while True:
            userUpdate = input("Enter new Name (Max 20 characters): ")
            if len(userUpdate) <= 20 and len(userUpdate) > 1:
                break

    # Updating Table
    if index == 0:
        query = "UPDATE songs SET Name = '"+userUpdate+"' WHERE songID = '"+songData[0]+"';"
    elif index == 1:
        query = "UPDATE songs SET Artist = '"+userUpdate+"' WHERE songID = '"+songData[0]+"';"
    elif index == 2:
        query = "UPDATE songs SET Album = '"+userUpdate+"' WHERE songID = '"+songData[0]+"';"
    elif index == 3:
        query = "UPDATE songs SET releaseDate = '"+userUpdate+"' WHERE songID = '"+songData[0]+"';"
    else:
        query = "UPDATE songs SET Explicit = '"+userUpdate+"' WHERE songID = '"+songData[0]+"';"

    db_ops.changeRecord(query)

def removeSong():
    while True:
        songName = input("Enter name of song you wish to remove: ")
        if len(songName) <= 20 and len(songName) > 1:
            break
        print("Must be 20 characters or less...")

    tempDict = {"val1":songName}
    query = "SELECT songID FROM songs WHERE Name = :val1;"
    songID = db_ops.wholeRecordDictionary(query, tempDict)
    if len(songID) == 0:
        print("Song not found...")
        return
    songID = songID[0][0]
    
    # Double check they want to delete this record
    print("Are you sure you want to delete this song?")
    print("Enter 0 to go back to menu, 1 to delete this song")
    userChoice = helper.get_choice([0,1])
    if userChoice == 0:
        return

    # User is sure, delete song
    tempDict2 = {"val1":songID}
    query = "DELETE FROM songs WHERE songID = :val1;"
    db_ops.deleteRecordDictionary(query, tempDict2)
    print("Record '"+songName+"' sucessfully deleted...")


def removeAllWithNull():
    # Check to ensure user wants to do this
    print("Are you sure you want to delete all songs with a null Value?")
    print("Enter 0 to go back to menu, 1 to continue")
    userChoice = helper.get_choice([0,1])
    if userChoice == 0:
        return

    attributes = ["Name", "Artist", "Album", "releaseDate", "Genre", "Explicit", \
        "Duration", "Energy", "Danceability", "Acousticness", "Liveness", "Loudness"]
    for attribute in attributes:
        query = "DELETE FROM songs WHERE "+attribute+" is NULL;" 
        db_ops.deleteRecord(query)
    print("Records sucessfully deleted...")
    


# main program
pre_process()
start_screen()
while True:
    user_choice = options()
    if user_choice == 1:
        search_by_artist()
    elif user_choice == 2:
        search_by_genre()
    elif user_choice == 3:
        search_by_feature()
    elif user_choice == 4:
        updateInformation()
    elif user_choice == 5:
        removeSong()
    elif user_choice == 6:
        removeAllWithNull()
    elif user_choice == 7:
        print("Goodbye!")
        break

db_ops.destructor()
