from DataGrabber import DataGrabber
from DeleteRecords import DeleteRecords
from UpdateRecords import UpdateRecords
from DisplayData import DisplayData
from dbOperations import dbOperations
from AddRecords import AddRecords
from helper import helper

# Update Data Base upon startup
def updateDB(dbOps):
    print("Updating Database...")
    DataGrabber.updateDatabase(dbOps)
    print("Database updated...\n")

# Main Menu
def displayMenu(dbOps):
    options = [1, 2, 3, 4, 5, 6]
    print("----Welcome to the NBA Database!---- \nPlease choose from the options below:")
    print("1) Display Data \n2) Query Data \n3) Add Records \n4) Update Records \n5) Delete Records \n6) Exit Program")
    userChoice = helper.get_choice(options)

    if userChoice == 1:
        displayData(dbOps)
    elif userChoice == 2:
        queryData(dbOps)
    elif userChoice == 3:
        addRecords(dbOps)
    elif userChoice == 4:
        updateRecords(dbOps)
    elif userChoice == 5:
        deleteRecords(dbOps)
    elif userChoice == 6:
        # Exit Program
        return False
    return True

# Secondary Menu - Displaying Records
def displayData(dbOps):
    options = [1, 2, 3, 4, 5]
    print("\nWhat Kind of Data are you looking for?")
    print("1) Player data \n2) Player stats \n3) Team data \n4) Team stats \n5) Return to Menu")
    userChoice = helper.get_choice(options)

    if userChoice == 1:
        DisplayData.playerData(dbOps)
    elif userChoice == 2:
        DisplayData.playerStats(dbOps)
    elif userChoice == 3:
        DisplayData.teamData(dbOps)
    elif userChoice == 4:
        DisplayData.teamStats(dbOps)
    elif userChoice == 5:
        print()
            
# Secondary Menu - Query Records
def queryData(dbOps):
    options = [1, 2, 3, 4, 5, 6]
    print("\What kind of Query would you like to do?")
    print("1) Player \n2) PlayerStats \n3) Team \n4) TeamStats \n5) Game \n6) Return to Menu")
    userChoice = helper.get_choice(options)
    
    
# Secondary Menu - Add Records to DB
def addRecords(dbOps):
    options = [1, 2, 3, 4, 5, 6]
    print("\nWhat Table do you want to add a record to?")
    print("1) Player \n2) PlayerStats \n3) Team \n4) TeamStats \n5) Game \n6) Return to Menu")
    userChoice = helper.get_choice(options)

    if userChoice == 1:
        AddRecords.addPlayer(dbOps)
    elif userChoice == 2:
        AddRecords.addPlayerStats(dbOps)
    elif userChoice == 3:
        AddRecords.addTeam(dbOps)
    elif userChoice == 4:
        AddRecords.addTeamStats(dbOps)
    elif userChoice == 5:
        AddRecords.addGame(dbOps)
    elif userChoice == 6:
        print()

# Secondary Menu - Update Records in DB
def updateRecords(dbOps):
    print("\nIn which table do you want to modify a record?")
    print("1) Player \n2) PlayerStats \n3) Team \n4) TeamStats \n5) Game \n6) Return to Menu")
    userChoice = helper.get_choice([1, 2, 3, 4, 5, 6])

    if userChoice == 1:
        UpdateRecords.updatePlayer(dbOps)
    elif userChoice == 2:
        UpdateRecords.updatePlayerStats(dbOps)
    elif userChoice == 3:
        UpdateRecords.updateTeam(dbOps)
    elif userChoice == 4:
        UpdateRecords.updateTeamStats(dbOps)
    elif userChoice == 5:
        UpdateRecords.updateGame(dbOps)
    elif userChoice == 6:
        print()

# Secondary Menu - Delete Records from DB - Incorporates Commit and Rollback
def deleteRecords(dbOps):
    print("\nFrom which table would you like to delete records?")
    print("1) Player \n2) PlayerStats \n3) Team \n4) TeamStats \n5) Game \n6) Return to Menu")
    userChoice = helper.get_choice([1,2,3,4,5,6])

    if userChoice == 1:
        DeleteRecords.deletePlayer(dbOps)
    elif userChoice == 2:
        DeleteRecords.deletePlayerStats(dbOps)
    elif userChoice == 3:
        DeleteRecords.deleteTeam(dbOps)
    elif userChoice == 4:
        DeleteRecords.deleteTeamStats(dbOps)
    elif userChoice == 5:
        DeleteRecords.deleteGame(dbOps)
    elif userChoice == 6:
        print()

# Main Function ----------------------------------------
def main():
    # Establish connection to Databse
    dbOps = dbOperations()

    # Update Database upon startup
    #updateDB(dbOps)

    # TESTING SECTION -------------
    DataGrabber.updateGame(dbOps)
    # -----------------------------

    # Program Loop
    while displayMenu(dbOps):
        print()
   
    dbOps.destructor()
    print("\nThank you for using NBA Database!")
    print("Now exiting...")
# ------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()