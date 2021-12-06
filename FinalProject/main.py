from DataGrabber import DataGrabber
from DisplayData import DisplayData
from dbOperations import dbOperations
from AddRecords import AddRecords
from helper import helper

# Update Data Base upon startup
def updateDB(dbOps):
    print("Updating Database...")
    DataGrabber.updateDatabase(dbOps)
    print("Database updated...")

# Main Menu
def displayMenu(dbOps):
    options = [1, 2, 3, 4, 5, 6]
    print("----Welcome to the NBA Database!---- \nPlease choose from the options below:")
    print("1) Display Data \n2) Query Data \n3) Add Records \n4) Update Records \n5) Delete Records \n6) Exit Program")
    userChoice = helper.get_choice(options)

    if userChoice == 1:
        displayData(dbOps)
    elif userChoice == 2:
        queryData()
    elif userChoice == 3:
        addRecords(dbOps)
    elif userChoice == 4:
        updateRecords()
    elif userChoice == 5:
        deleteRecords()
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
def queryData():
    print("")
    
# Secondary Menu - Add Records to DB
def addRecords(dbOps):
    options = [1, 2, 3, 4, 5]
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
def updateRecords():
    print("")

# Secondary Menu - Delete Records from DB
def deleteRecords():
    print("")

# Main Function ----------------------------------------
def main():
    # Establish connection to Databse
    dbOps = dbOperations()

    # Update Database upon startup
    #updateDB(dbOps)

    # TESTING SECTION -------------
    #AddRecords.addPlayer(dbOps)
    # -----------------------------

    # Program Loop
    while displayMenu(dbOps):
        print()
   
    dbOps.destructor()
    print("Thank you for using NBA Database!")
    print("Now exiting...")
# ------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()