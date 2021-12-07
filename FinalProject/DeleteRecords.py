from helper import helper

class DeleteRecords:
    @staticmethod
    def deletePlayer(dbOps):
        attr = ["ID", "Full Name", "First Name", "Last Name", "isActive"]
        print("Which player would you like to delete?")
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            
            print("Are you sure you want to delete the above record?")
            print("This will also delete the player's stats...")
            if (input("Y/N: ")) == 'Y':
                # First delete from playerstats (if it exists)
                try:
                    query = "DELETE FROM playerstats WHERE playerID = %s;"
                    dbOps.executeQuery(query,(ID,))
                except:
                    pass

                # Then delete from player
                query = "DELETE FROM player WHERE playerID = %s;"
                dbOps.executeQuery(query,(ID,))
                print("Player with ID: " + str(ID) + " successfully deleted.")
                return
            
            else:
                print("Operation Cancelled returning to menu...")
                return

        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM player WHERE fullName = %s;"
            pInfo = dbOps.getRecord(query, (name,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            
            print("Are you sure you want to delete the above record?")
            print("This will also delete the player's stats...")
            if (input("Y/N: ")) == 'Y':
                # First delete from playerstats (if it exists)
                try:
                    query = "DELETE FROM playerstats WHERE playerID = %s;"
                    dbOps.executeQuery(query,(pInfo[0],))
                except:
                    pass

                # Then delete from player
                query = "DELETE FROM player WHERE playerID = %s;"
                dbOps.executeQuery(query, (pInfo[0],))
                print("Player with fullName: " + name + " successfully deleted.")
                return

            else:
                print("Operation Cancelled returning to menu...")
                return


    @staticmethod
    def deletePlayerStats(dbOps):
        attr = ["pID", "timeFrame", "PTS", "AST", "REB", "PIE"]
        print("Which player's stats would you like to delete?")
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM player WHERE playerID = %s;"
            pInfo = dbOps.getRecord(query, (ID,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return
            helper.formattedDisplay(attr, pInfo)
            
            print("Are you sure you want to delete the above record?")
            if (input("Y/N: ")) == 'Y':
                # Delete from playerstats
                query = "DELETE FROM playerstats WHERE playerID = %s;"
                dbOps.executeQuery(query,(ID,))
                print("Player with ID: " + str(ID) + " successfully deleted.")
                return
            
            else:
                print("Operation Cancelled returning to menu...")
                return

        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM player WHERE fullName = %s;"
            pInfo = dbOps.getRecord(query, (name,))
            if pInfo == None:
                print("\nPlayer Not Found...\n")
                return

            query = "SELECT * FROM playerstats WHERE playerID = %s;"
            pStats = dbOps.getRecord(query, (pInfo[0]))
            helper.formattedDisplay(attr, pStats)
            
            print("Are you sure you want to delete the above record?")
            if (input("Y/N: ")) == 'Y':
                # Delete from playerstats
                query = "DELETE FROM player WHERE playerID = %s;"
                dbOps.executeQuery(query, (pInfo[0],))
                print("Player with fullName: " + name + " successfully deleted.")

            else:
                print("Operation Cancelled returning to menu...")
                return


    @staticmethod
    def deleteTeam(dbOps):
        attr = ["teamID", "Name", "Abbreviation", "Nickname", "City", "State", "YearFounded"]
        print("Which team would you like to delete?")
        print("\nSearch by: \n1) ID \n2) Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM team WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)

            print("Are you sure you want to delete the above record?")
            print("This will also delete the team's stats...")
            if (input("Y/N: ")) == 'Y':
                # First delete from playerstats (if it exists)
                try:
                    query = "DELETE FROM teamstats WHERE teamID = %s;"
                    dbOps.executeQuery(query,(ID,))
                except:
                    pass

                # Then delete from player
                query = "DELETE FROM team WHERE teamID = %s;"
                dbOps.executeQuery(query,(ID,))
                print("Team with ID: " + str(ID) + " successfully deleted.")
                return
            
            else:
                print("Operation Cancelled returning to menu...")
                return

        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM team WHERE name = %s;"
            tInfo = dbOps.getRecord(query, (name,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)
            
            print("Are you sure you want to delete the above record?")
            print("This will also delete the teams's stats...")
            if (input("Y/N: ")) == 'Y':
                # First delete from teamstats (if it exists)
                try:
                    query = "DELETE FROM teamstats WHERE teamID = %s;"
                    dbOps.executeQuery(query,(tInfo[0],))
                except:
                    pass

                # Then delete from team
                query = "DELETE FROM team WHERE playerID = %s;"
                dbOps.executeQuery(query, (tInfo[0],))
                print("Player with fullName: " + name + " successfully deleted.")
                return

            else:
                print("Operation Cancelled returning to menu...")
                return


    @staticmethod
    def deleteTeamStats(dbOps):
        attr = ["ID", "TimeFrame", "Wins", "Losses", "WinPCT", "FG_PCT", "FG3_PCT", "REB", "AST", "BLK", "PTS"]
        print("Which team's stats would you like to delete?")
        print("\n1) Search By ID\n2) Search By Full Name")
        userChoice = helper.get_choice([1, 2])

        if userChoice == 1:
            ID = int(input("Enter ID: "))
            query = "SELECT * FROM teamstats WHERE teamID = %s;"
            tInfo = dbOps.getRecord(query, (ID,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return
            helper.formattedDisplay(attr, tInfo)

            print("Are you sure you want to delete the above record?")
            print("This will also delete the team's stats...")
            if (input("Y/N: ")) == 'Y':
                # Delete from teamstats
                query = "DELETE FROM teamstats WHERE teamID = %s;"
                dbOps.executeQuery(query,(ID,))
                print("Team's stats with ID: " + str(ID) + " successfully deleted.")
                return
            
            else:
                print("Operation Cancelled returning to menu...")
                return

        elif userChoice == 2:
            name = input("Enter Full Name: ")
            query = "SELECT * FROM team WHERE name = %s;"
            tInfo = dbOps.getRecord(query, (name,))
            if tInfo == None:
                print("\nTeam Not Found...\n")
                return

            query = "SELECT * FROM teamstats WHERE teamID = %s;"
            tStats = dbOps.getRecord(query, (tInfo[0]))
            helper.formattedDisplay(attr, tStats)
            
            print("Are you sure you want to delete the above record?")
            if (input("Y/N: ")) == 'Y':
                # Delete from teamstats
                query = "DELETE FROM teamstats WHERE playerID = %s;"
                dbOps.executeQuery(query, (tInfo[0],))
                print("Player with fullName: " + name + " successfully deleted.")
                return

            else:
                print("Operation Cancelled returning to menu...")
                return

    @staticmethod
    def deleteGame():
        print()