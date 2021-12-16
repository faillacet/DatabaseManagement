from DisplayData import DisplayData
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
                dbOps.executeQueryTN("START TRANSACTION;")
                query = "DELETE FROM playerstats WHERE playerID = %s;"
                dbOps.executeQuery(query,(ID,))

                # Then delete from player
                try:
                    query = "DELETE FROM player WHERE playerID = %s;"
                    dbOps.executeQueryT(query,(ID,))
                    dbOps.commit()
                    print("Player with ID: " + str(ID) + " successfully deleted.")
                except:
                    dbOps.rollback()
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
                dbOps.executeQueryTN("START TRANSACTION;")
                query = "DELETE FROM playerstats WHERE playerID = %s;"
                dbOps.executeQuery(query,(pInfo[0],))
                
                # Then delete from player
                try:
                    query = "DELETE FROM player WHERE playerID = %s;"
                    dbOps.executeQueryT(query, (pInfo[0],))
                    dbOps.commit()
                    print("Player with fullName: " + name + " successfully deleted.")
                except:
                    dbOps.rollback()
                
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
                # First delete from teamstats (if it exists)
                dbOps.executeQueryTN("START TRANSACTION;")
                query = "DELETE FROM teamstats WHERE teamID = %s;"
                dbOps.executeQuery(query,(ID,))

                # Then delete from team
                try:
                    query = "DELETE FROM team WHERE teamID = %s;"
                    dbOps.executeQuery(query,(ID,))
                    dbOps.commit()
                    print("Team with ID: " + str(ID) + " successfully deleted.")
                except:
                    dbOps.rollback()

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
            print("This will also delete the teams's stats, associated games, and unlink players from this team...")
            if (input("Y/N: ")) == 'Y':
                # First delete from teamstats (if it exists)
                dbOps.executeQueryTN("START TRANSACTION;")
                try:
                    query = "DELETE FROM teamstats WHERE teamID = %s;"
                    dbOps.executeQuery(query,(tInfo[0],))
                
                    # Now remove games
                    query = "DELETE FROM game WHERE teamID = %s;"
                    dbOps.executeQuery(query, (tInfo[0],))
                    query = "DELETE FROM game WHERE matchupteamID = %s"
                    dbOps.executeQuery(query, (tInfo[0],))

                    # Now unlink players
                    query = "UPDATE player SET teamID = NULL WHERE teamID = %s"
                    dbOps.executeQuery(query, (tInfo[0],))
                    # Then delete from team
                    
                    query = "DELETE FROM team WHERE teamID = %s;"
                    dbOps.executeQueryT(query, (tInfo[0],))
                    dbOps.commit()
                    print("Team with name: " + name + " successfully deleted.")
                except:
                    dbOps.rollback()
             
       

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
    def deleteGame(dbOps):
        attr = ["gameID", "teamID", "matchupteamID", "homeGame", "seasonID", "gameDate", "WL", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("Which Game's stats would you like to delete?")
        gInfo = DisplayData.gameData(dbOps)

        print("Are you sure you want to delete the record?")
        if (input("Y/N: ")) == 'Y':
            # delete from game
            query = "DELETE FROM game WHERE gameID = %s;"
            dbOps.executeQuery(query, (gInfo[0],))
            print ("game with gameID: " + str(gInfo[0]) + " successfully delete.")
            return
        else:
            print("Operation Cancelled returning to menu...")
            return
