from DataGrabber import DataGrabber
from dbOperations import dbOperations
from helper import helper

def updateDB(dbOps):
    print("Updating Database...")
    DataGrabber.updateDatabase(dbOps)
    print("Database updated...")

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
    print("What Kind of Data are you looking for?")
    print("1) Player data \n2) Player stats \n3) Team data \n4) Team stats \n5) Game Data \n6) Return to Menu")
    userChoice = helper.get_choice(options)
    while True:
        # Player Data
        if userChoice == 1:
            print("Search by: \n1) ID \n2) Full Name")
            userChoice2 = helper.get_choice([1, 2])
            if userChoice2 == 1:
                # Search by ID
                ID = int(input("Enter ID: "))
                query = "SELECT * FROM player WHERE playerID = "+str(ID)+";"
                pInfo = dbOps.getRecord(query)
                if pInfo == None:
                    print("Player Not Found...\n")
                    break
                print("ID, Full Name, First Name, Last Name, isActive")
                print(pInfo)
                print()
            elif userChoice2 == 2:
                # Search By Full Name
                firstName, lastName = input("Enter Full Name: ").split()
                query = "SELECT * FROM player WHERE fullName = '"+firstName+" "+lastName+"';"
                pInfo = dbOps.getRecord(query)
                if pInfo == None:
                    print("Player Not Found...")
                    break
                print("ID, Full Name, First Name, Last Name, isActive")
                print(pInfo)
                print()
            break
        # Player Stats
        elif userChoice == 2:
            print("Search by: \n1) ID \n2) Full Name")
            userChoice2 = helper.get_choice([1, 2])
            if userChoice2 == 1:
                # Search by ID
                ID = int(input("Enter ID: "))
                query = "SELECT * FROM playerstats WHERE playerID = "+str(ID)+";"
                pInfo = dbOps.getRecord(query)
                if pInfo == None:
                    # Check API
                    if DataGrabber.getPlayerStats(dbOps, ID) == True:
                        pInfo = dbOps.getRecord(query)
                        print("pID, timeframe, pts, ast, reb, pie")
                        print(pInfo)
                        print()
                    else:
                        print("Player Not Found...\n")
                        break
                else:
                    print("pID, timeframe, pts, ast, reb, pie")
                    print(pInfo)
                break
            elif userChoice2 == 2:
                # Search by Full Name
                firstName, lastName = input("Enter Full Name: ").split()
                query = "SELECT * FROM player WHERE fullName = '"+firstName+" "+lastName+"';"
                pID = dbOps.getRecord(query)[0]
                if pID == None:
                    print("Player not found...")
                    break
                else:
                    query = "SELECT * FROM playerstats WHERE playerID = "+str(pID)+";"
                    pInfo = dbOps.getRecord(query)
                    if pInfo == None:
                        # Check API
                        if DataGrabber.getPlayerStats(dbOps, pID) == True:
                            pInfo = dbOps.getRecord(query)
                            print("pID, timeframe, pts, ast, reb, pie")
                            print(pInfo)
                            print()
                        else:
                            print("Player Not Found...\n")
                            break
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