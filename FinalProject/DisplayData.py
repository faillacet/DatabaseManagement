from helper import helper
from DataGrabber import DataGrabber

class DisplayData:
    @staticmethod
    def playerData(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["playerID", "teamID", "fullName", "firstName", "lastName", "isActive"]

        if userChoice == 1:
            # Search by ID
            try:
                ID = int(input("Enter ID: "))
            except:
                print("Please use an integer value...\n")
                return
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            return pInfo

        # Search By Full Name
        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM player WHERE fullName = %s;"
            pInfo = dbOps.getRecord(query, (name,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            return pInfo

    @staticmethod
    def playerStats(dbOps):
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["playerID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]

        if userChoice == 1:
            # Search by ID
            try:
                ID = int(input("Enter ID: "))
            except:
                print("Please use an integer value...\n")
                return
            query = "SELECT * FROM playerstats WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                # Check API
                if DataGrabber.getPlayerStats(dbOps, ID) == True:
                    pInfo = dbOps.getRecord(query, None)
                    helper.formattedDisplay(attr, pInfo)
                    return pInfo
                else:
                    print("\nPlayer Not Found...\n")
                    return
            else:
                helper.formattedDisplay(attr, pInfo)
                return pInfo

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
                        return pInfo
                    else:
                        print("\nPlayer Not Found...\n")
                        return
                else:
                    helper.formattedDisplay(attr, pInfo)
                    return pInfo

    @staticmethod
    def teamData(dbOps):
        print("\n1) Display All: \n2) Search By ID\n3) Search By Full Name")
        userChoice = helper.get_choice([1, 2, 3])
        attr = ["teamID", "Name", "Abbreviation", "Nickname", "City", "State", "YearFounded"]

        if userChoice == 1:
            # Display All
            query = "SELECT * FROM vAllTeams;"
            teams = dbOps.getRecords(query)
            print("\nname, abbreviation, nickname, city, state, yearfounded")
            helper.prettyPrint(teams)
            return

        elif userChoice == 2:
            try:
                ID = int(input("Enter ID: "))
            except:
                print("Please use an integer value...\n")
                return
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
        attr = ["teamID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]

        if userChoice == 1:
            # Search by ID
            try:
                ID = int(input("Enter ID: "))
            except:
                print("Please use an integer value...\n")
                return
            query = "SELECT * FROM teamstats WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                # Try to pull from API
                if DataGrabber.getTeamStats(dbOps, ID) == True:
                    tInfo = dbOps.getRecord(query, (ID,))
                    helper.formattedDisplay(attr, tInfo)
                    return tInfo
                else:
                    print("\Team Not Found...\n")
                    return
            else:
                helper.formattedDisplay(attr, tInfo)
                return tInfo

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
                        return tInfo
                    else:
                        print("\nTeam Not Found...\n")
                        return
                else:
                    helper.formattedDisplay(attr, tInfo)
                    return tInfo

    @staticmethod
    def gameData(dbOps):
        attr = ["gameID", "teamID", "matchupteamID", "homeGame", "seasonID", "gameDate", "WL", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("\n1) Search By ID\n2) Search By Both Teams")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            # Search By ID
            try:
                ID = int(input("Enter ID: "))
            except:
                print("Please enter a valid integer...\n")
                return
            query = "SELECT * FROM game WHERE gameID = %s;"
            gInfo = dbOps.getRecord(query, (ID,))
            if gInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, gInfo)
            return gInfo

        else:
            team1 = input("Enter Full Name of first team: ")
            team2 = input("Enter Full Name of second team: ")

            try:
                query = "SELECT teamID FROM team WHERE name = %s"
                team1ID = dbOps.getRecord(query, (team1,))[0]
                team2ID = dbOps.getRecord(query, (team2,))[0]
            except:
                print("Team not found...\n")
                return

            try:
                query = "SELECT * FROM game WHERE teamID = " + str(team1ID) + " AND matchupteamID = " + str(team2ID) + ";"
                gInfo = dbOps.getRecord(query, None)
            except:
                print("Game not found...\n")
                return

            helper.formattedDisplay(attr, gInfo)
            return gInfo

