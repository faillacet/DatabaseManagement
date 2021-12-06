from helper import helper
from DataGrabber import DataGrabber

class DisplayData:
    @staticmethod
    def playerData(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["ID", "Full Name", "First Name", "Last Name", "isActive"]

        if userChoice == 1:
            # Search by ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
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
            helper.formattedDisplay(attr, pInfo)
            return

    @staticmethod
    def playerStats(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["pID", "timeFrame", "PTS", "AST", "REB", "PIE"]

        if userChoice == 1:
            # Search by ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM playerstats WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                # Check API
                if DataGrabber.getPlayerStats(dbOps, ID) == True:
                    pInfo = dbOps.getRecord(query, None)
                    helper.formattedDisplay(attr, pInfo)
                else:
                    print("\nPlayer Not Found...\n")
                    return
            else:
                helper.formattedDisplay(attr, pInfo)
                return

        elif userChoice == 2:
            # Search by Full Name
            name = input("Enter Full Name: ")
            query = "SELECT playerID FROM player WHERE fullName = %s;"
            pID = dbOps.getRecord(query, (name,))
            if pID == None:
                print("\nPlayer not found...\n")
                return
            else:
                pID = pID[0]
                query = "SELECT * FROM playerstats WHERE playerID = %s;"
                pInfo = dbOps.getRecord(query, (pID,))
                if pInfo == None:
                    # Check API
                    if DataGrabber.getPlayerStats(dbOps, pID) == True:
                        pInfo = dbOps.getRecord(query, (pID,))
                        helper.formattedDisplay(attr, pInfo)
                    else:
                        print("\nPlayer Not Found...\n")
                        return
                else:
                    helper.formattedDisplay(attr, pInfo)
                    return

    @staticmethod
    def teamData(dbOps):
        print("\n1) Display All: \n2) Search By ID\n3) Search By Full Name")
        userChoice = helper.get_choice([1, 2, 3])
        attr = ["teamID", "Name", "Abbreviation", "Nickname", "City", "State", "YearFounded"]

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
            helper.formattedDisplay(attr, tInfo)
            return

        elif userChoice == 3:
            name = input("Enter Full Team Name: ")
            query = "SELECT * FROM team WHERE name = %s;"
            tInfo = dbOps.getRecord(query, (name,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)
            return

    @staticmethod
    def teamStats(dbOps):
        print("\n1) Search By ID\n2) Search By Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["ID", "TimeFrame", "Wins", "Losses", "WinPCT", "FG_PCT", "FG3_PCT", "REB", "AST", "BLK", "PTS"]

        if userChoice == 1:
            # Search by ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM teamstats WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                # Try to pull from API
                if DataGrabber.getTeamStats(dbOps, ID) == True:
                    tInfo = dbOps.getRecord(query, (ID,))
                    helper.formattedDisplay(attr, tInfo)
                else:
                    print("\Team Not Found...\n")
                    return
            else:
                helper.formattedDisplay(attr, tInfo)
                return

        elif userChoice == 2:
            # Search by Full Name
            name = input("Enter Full Name: ")
            query = "SELECT teamID FROM team WHERE name = %s;"
            tID = dbOps.getRecord(query, (name,))
            if tID == None:
                print("\Team not found...\n")
                return
            else:
                tID = tID[0]
                query = "SELECT * FROM teamstats WHERE teamID = %s;"
                tInfo = dbOps.getRecord(query, (tID,))
                if tInfo == None:
                    # Check API
                    if DataGrabber.getTeamStats(dbOps, tID) == True:
                        tInfo = dbOps.getRecord(query, (tID,))
                        helper.formattedDisplay(attr, tInfo)
                    else:
                        print("\nTeam Not Found...\n")
                        return
                else:
                    helper.formattedDisplay(attr, tInfo)
                    return

