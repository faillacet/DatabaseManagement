from helper import helper

class UpdateRecords:
    @staticmethod
    def updatePlayer(dbOps):
        print("\nWhich player would you like to modify?")
        print("Search by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])
        attr = ["playerID", "fullName", "firstName", "lastName", "isActive"]
        
        if userChoice == 1:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            
        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM player WHERE fullName = %s;"
            pInfo = dbOps.getRecord(query, (name,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)

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
        print()

    @staticmethod
    def updateTeam(dbOps):
        print()

    @staticmethod
    def updateTeamStats(dbOps):
        print()

    @staticmethod
    def updateGame(dbOps):
        print()