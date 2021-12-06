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
            print("Player Successfully Updated! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")       
        
        return
        
    @staticmethod
    def updateTeam(dbOps):
        print()

    @staticmethod
    def updateTeamStats(dbOps):
        print()

    @staticmethod
    def updateGame(dbOps):
        print()