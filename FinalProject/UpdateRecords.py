from helper import helper
from DisplayData import DisplayData

class UpdateRecords:
    @staticmethod
    def updatePlayer(dbOps):
        attr = ["playerID", "teamID", "fullName", "firstName", "lastName", "isActive"]
        print("\nWhich player would you like to modify?")
        pInfo = DisplayData.playerData(dbOps)
        if pInfo == None:
            return

        # Player Found and Displayed - Now modify...
        attr2 = ["playerID (int)", "teamID (int)", "Full Name (string)", "First Name (string)", "Last Name (string)", "isActive (bool- 0 or 1)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5, 6])
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
        attr = ["playerID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("Which player's stats would you like to modify?")
        pStats = DisplayData.playerStats(dbOps)
        if pStats == None:
            return

        # Player stats found and Displayed - Now modify
        print("\nWhich value would you like to modify?")
        counter = 0
        choiceCount = []
        for x in range(len(attr)):
            print(str(x + 1) + ") " + attr[x])
            counter = counter + 1
            choiceCount.append(counter)

        userChoice = helper.get_choice(choiceCount)
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
        attr2 = ["teamID (int)", "Team Name (string)", "Abbreviation (string)", "Nickname (string)", "City (string)", "State (string)", "YearFounded (string)"]
        print("\nWhich value would you like to modify?")
        for x in range(len(attr2)):
            print(str(x + 1) + ") " + attr2[x])

        userChoice = helper.get_choice([1, 2, 3, 4, 5, 6, 7])
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
        attr = ["teamID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("Which team's stats would you like to modify?")
        tStats = DisplayData.teamStats(dbOps)
        if tStats == None:
            return

        # Team stats found and displayed - Now modify
        counter = 0
        choiceCount = []
        for x in range(len(attr)):
            print(str(x + 1) + ") " + attr[x])
            counter = counter + 1
            choiceCount.append(counter)

        userChoice = helper.get_choice(choiceCount)
        userInput = input("Enter new value: ")
        query = "UPDATE teamstats SET " + attr[userChoice - 1] + " = %s WHERE teamID = " + str(tStats[0]) + ";"

        # Attempt to push change
        try:
            dbOps.executeQuery(query, (userInput,))
            print("TeamStats Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       
        
        return

    @staticmethod
    def updateGame(dbOps):
        attr = ["gameID", "teamID", "matchupteamID", "homeGame", "seasonID", "gameDate", "WL", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("Which game would you like to view?")
        gStats = DisplayData.gameData(dbOps)
        if gStats == None:
            return

        # Game found and displayed - Now modify
        counter = 0
        choiceCount = []
        for x in range(len(attr)):
            print(str(x + 1) + ") " + attr[x])
            counter = counter + 1
            choiceCount.append(counter)

        userChoice = helper.get_choice(choiceCount)
        userInput = input("Enter new value: ")
        query = "UPDATE game SET " + attr[userChoice - 1] + " = %s WHERE gameID = " + str(gStats[0]) + ";"

        try:
            dbOps.executeQuery(query, (userInput,))
            print("Game Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")      

        return