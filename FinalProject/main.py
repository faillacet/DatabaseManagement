from DataGrabber import DataGrabber
from DisplayData import DisplayData
from dbOperations import dbOperations
from helper import helper

#
def updateDB(dbOps):
    print("Updating Database...")
    DataGrabber.updateDatabase(dbOps)
    print("Database updated...")

# Main Menu
def displayMenu():
    options = [1, 2, 3, 4, 5, 6]
    print("----Welcome to the NBA Database!---- \nPlease choose from the options below:")
    print("1) Display Data")
    print("2) Query Data")
    print("3) Add Records")
    print("4) Update Records")
    print("5) Delete Records")
    print("6) Exit Program")
    return helper.get_choice(options)

def displayData(dbOps):
    options = [1, 2, 3, 4, 5, 6]
    print("\nWhat Kind of Data are you looking for?")
    print("1) Player data \n2) Player stats \n3) Team data \n4) Team stats \n5) Game Data \n6) Return to Menu")
    userChoice = helper.get_choice(options)

    # Menu Loop
    while True:
        # Player Data
        if userChoice == 1:
            DisplayData.playerData(dbOps)
            break
        # Player Stats
        elif userChoice == 2:
            DisplayData.playerStats(dbOps)
            break
        elif userChoice == 3:
            DisplayData.teamData(dbOps)
            break
        elif userChoice == 6:
            break


            
def queryData():
    print("")
    
def addRecords():
    print("")

def updateRecords():
    print("")

def deleteRecords():
    print("")

# Main Function ----------------------------------------
def main():
    # Establish connection to Databse
    dbOps = dbOperations()

    # Update Database upon startup
    #updateDB(dbOps)

    # TESTING SECTION -------------
    #DisplayData.teamStats(dbOps)
    # -----------------------------

    # Program Loop
    while True:
        userChoice = displayMenu()
        if userChoice == 1:
            displayData(dbOps)
        elif userChoice == 2:
            queryData()
        elif userChoice == 3:
            addRecords()
        elif userChoice == 4:
            updateRecords()
        elif userChoice == 5:
            deleteRecords()
        elif userChoice == 6:
            # Exit Program
            break;
    dbOps.destructor()
    print("Thank you for using NBA Database!")
    print("Now exiting...")
# ------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()