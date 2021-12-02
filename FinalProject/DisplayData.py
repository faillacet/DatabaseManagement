from helper import helper
from DataGrabber import DataGrabber

class DisplayData:
    @staticmethod
    def playerData(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            # Search by ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            print("\nID, Full Name, First Name, Last Name, isActive")
            print(pInfo)
            print()
            return

        # Search By Full Name
        elif userChoice == 2:
            try:
                name = input("Enter Full Name: ")
            except:
                print("\nPlayer Not found...\n")
                return
            query = "SELECT * FROM player WHERE fullName = %s;"
            pInfo = dbOps.getRecord(query, (name,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            print("\nID, Full Name, First Name, Last Name, isActive")
            print(pInfo)
            print()
            return

    @staticmethod
    def playerStats(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            # Search by ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM playerstats WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                # Check API
                if DataGrabber.getPlayerStats(dbOps, ID) == True:
                    pInfo = dbOps.getRecord(query, None)
                    print("\npID, timeframe, pts, ast, reb, pie")
                    print(pInfo)
                    print()
                else:
                    print("\nPlayer Not Found...\n")
                    return
            else:
                print("\npID, timeframe, pts, ast, reb, pie")
                print(pInfo)
                print()
                return

        elif userChoice == 2:
            # Search by Full Name
            name = input("Enter Full Name: ")
            query = "SELECT playerID FROM player WHERE fullName = %s;"
            pID = dbOps.getRecord(query, (name,))[0]
            if pID == None:
                print("\nPlayer not found...\n")
                return
            else:
                query = "SELECT * FROM playerstats WHERE playerID = %s;"
                pInfo = dbOps.getRecord(query, (pID,))
                if pInfo == None:
                    # Check API
                    if DataGrabber.getPlayerStats(dbOps, pID) == True:
                        pInfo = dbOps.getRecord(query, (pID,))
                        print("\npID, timeframe, pts, ast, reb, pie")
                        print(pInfo)
                        print()
                    else:
                        print("\nPlayer Not Found...\n")
                        return
                else:
                    print("\npID, timeframe, pts, ast, reb, pie")
                    print(pInfo)
                    print()
                    return

    @staticmethod
    def teamData(dbOps):
        print("\n1) Display All: \n2) Search By ID\n3) Search By Full Name")
        userChoice = helper.get_choice([1, 2, 3])

        if userChoice == 1:
            # Display All
            query = "SELECT * FROM team;"
            teams = dbOps.getRecords(query)
            print("\nteamID, name, abbreviation, nickname, city, state, yearfounded")
            helper.prettyPrint(teams)
            return

        elif userChoice == 2:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM team WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            print("\nteamID, name, abbreviation, nickname, city, state, yearfounded")
            print(tInfo)
            print()
            return

        elif userChoice == 3:
            name = input("Enter Full Team Name: ")
            query = "SELECT * FROM team WHERE name = %s;"
            tInfo = dbOps.getRecord(query, (name,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            print("\nteamID, name, abbreviation, nickname, city, state, yearfounded")
            print(tInfo)
            print()
            return

    @staticmethod
    def teamStats(dbOps):
        input1 = input()
        print(input1)

    @staticmethod
    def gameData(dbOps):
        print()

