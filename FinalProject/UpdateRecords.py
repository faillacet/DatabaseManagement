from helper import helper
from DataGrabber import DataGrabber
from DisplayData import DisplayData

class UpdateRecords:
    @staticmethod
    def updatePlayer(dbOps):
        attr = ["playerID", "fullName", "firstName", "lastName", "isActive"]
        print("\nWhich player would you like to modify?")
        pInfo = DisplayData.playerData(dbOps)
        if pInfo == None:
            return

        # Player Found and Displayed - Now modify...
        attr2 = ["pID (int)", "Full Name (string)", "First Name (string)", "Last Name (string)", "isActive (bool- 0 or 1)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5])
        userInput = input("Enter new value: ")
        query = "UPDATE player SET " + attr[userChoice - 1] + " = %s WHERE playerID = " + str(pInfo[0]) + ";"
        
        # Attempt to push change
        try:
            dbOps.executeQuery(query, (userInput,))
            print("Player Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       
        
        return

    @staticmethod
    def updatePlayerStats(dbOps):
        attr = ["playerID", "timeFrame", "points", "assists", "rebounds", "playerimpactestimate"]
        print("Which player's stats would you like to modify?")
        pStats = DisplayData.playerStats(dbOps)
        if pStats == None:
            print("test")
            return

        # Player stats found and Displayed - Now modify
        attr2 = ["playerID (int)", "timeFrame (string)", "PTS (float)", "AST (float)", "REB (float)", "PIE (float)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5, 6])
        userInput = input("Enter new value: ")
        query = "UPDATE playerstats SET " + attr[userChoice - 1] + " = %s WHERE playerID = " + str(pStats[0]) + ";"

        # Attempt to push change
        try:
            dbOps.executeQuery(query, (userInput,))
            print("PlayerStats Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       
        
        return
        
    @staticmethod
    def updateTeam(dbOps):
        attr = ["teamID", "name", "abbreviation", "nickname", "city", "state", "yearfounded"]
        print("Which team's record would you like to modify?")
        print("\n1) Search By ID\n2) Search By Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            # Search By ID
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM team WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)
            
        elif userChoice == 2:
            # Search by Full Name
            name = input("Enter Full Team Name: ")
            query = "SELECT * FROM team WHERE name = %s;"
            tInfo = dbOps.getRecord(query, (name,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)

        # Team Info found and displayed - Now modify
        attr2 = ["teamID (int)", "Team Name (string)", "Abbreviation (string)", "Nickname (string)", "City (string)", "YearFounded (string)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5, 6])
        userInput = input("Enter new value: ")
        query = "UPDATE team SET " + attr[userChoice - 1] + " = %s WHERE teamID = " + str(tInfo[0]) + ";"

        # Try to push change to DB
        try:
            dbOps.executeQuery(query, (userInput,))
            print("Team Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       

        return

    @staticmethod
    def updateTeamStats(dbOps):
        attr = ["teamID", "timeframe", "wins", "losses", "wPCT", "fgPCT", "fg3PCT", "rebounds", "assists", "blocks", "points"]
        print("Which team's stats would you like to modify?")
        tStats = DisplayData.teamStats(dbOps)
        if tStats == None:
            return

        # Team stats found and displayed - Now modify
        attr2 = ["teamID (int)", "timeframe (string)", "wins (int)", "losses (int)", "wPCT (float)", "fgPCT (float)", "fg3PCT (float)", 
                "rebounds (float)", "assists (float)", "blocks (float)", "points (float)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        userInput = input("Enter new value: ")
        query = "UPDATE teamstats SET " + attr[userChoice - 1] + " = %s WHERE playerID = " + str(tStats[0]) + ";"

        # Attempt to push change
        try:
            dbOps.executeQuery(query, (userInput,))
            print("TeamStats Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       
        
        return

    @staticmethod
    def updateGame(dbOps):
        print()