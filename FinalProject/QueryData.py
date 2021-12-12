from helper import helper

class QueryData:
    @staticmethod
    def displayTop5(dbOps):
        print("Display:\n1) Top 5 Players \n2) Top 5 Teams")
        userChoice = helper.get_choice([1,2])

        if userChoice == 1:
            attr = ["playerID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "blocks", "points"]
            print("Which category do you wish to stort by?")
            counter = 0
            choiceCount = []
            for x in range(len(attr)):
                if x == 0:
                    pass
                else:
                    print(str(x) + ") " + attr[x])
                    counter = counter + 1
                    choiceCount.append(counter)
            userChoice = helper.get_choice(choiceCount)

            query = "SELECT * from playerstats ORDER BY " + attr[userChoice] + " DESC LIMIT 10;"
            players = dbOps.getRecords(query)
            query = "SELECT fullName FROM player WHERE playerID = %s;"
            list = []
            for player in players:
                list.append(dbOps.getRecord(query, (player[0],)))

            print("\nTop 10 Active Players by " + attr[userChoice] + ":")
            for x in range(len(list)):
                print(str(x+1) + ") " + list[x][0] + " - " + attr[userChoice] + ": " + str(players[x][userChoice]))
            print()
            return

        elif userChoice == 2:
            attr = ["teamID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
            print("Which category do you wish to sort by?")
            counter = 0
            choiceCount = []
            for x in range(len(attr)):
                if x == 0:
                    pass
                else:
                    print(str(x) + ") " + attr[x])
                    counter = counter + 1
                    choiceCount.append(counter)
            userChoice = helper.get_choice(choiceCount)

            query = "SELECT * from teamstats ORDER BY " + attr[userChoice] + " DESC LIMIT 10;"
            teams = dbOps.getRecords(query)
            query = "SELECT name FROM team WHERE teamID = %s;"
            list = []
            for team in teams:
                list.append(dbOps.getRecord(query, (team[0],)))

            print("\nTop 10 Active Teams by " + attr[userChoice] + ":")
            for x in range(len(list)):
                print(str(x+1) + ") " + list[x][0] + " - " + attr[userChoice] + ": " + str(teams[x][userChoice]))
            print()
            return

    @staticmethod
    def chanceToWin(dbOps):
        # USES primitive algorithm to estimate chance of one team to win against another
        # based on previous games against eachother and overall stats
        print("This feature allows you to estimate win percent for one team against another.")
        print("This will display team one's chances to win against team two.")
        team1 = input("Enter First Team Name: ")
        team2 = input("Enter Second Team Name: ")

        # Find stats for both teams
        query = "SELECT * FROM teamstats WHERE teamID = (SELECT teamID FROM team WHERE name = %s);"
        team1Stats = dbOps.getRecord(query, (team1,))
        query2 = "SELECT * FROM teamstats WHERE teamID = (SELECT teamID FROM team WHERE name = %s);"
        team2Stats = dbOps.getRecord(query2, (team2,))
        if (team1Stats == None or team2Stats == None):
            print("Could not find stats for these two teams...\n")
            return

        # FOUND stats now find games between the two
        query = "SELECT * FROM game WHERE teamID = " + str(team1Stats[0]) + " AND matchupteamID = " + str(team2Stats[0]) + ";"
        games = dbOps.getRecords(query)
        if games == None:
            print("No games found between these two teams...\n")
            return
        query2 = "SELECT * FROM game WHERE teamID = " + str(team2Stats[0]) + " AND matchupteamID = " + str(team1Stats[0]) + ";"
        gamesReverse = dbOps.getRecords(query2)

        # Comparison Between games
        calc1 = 0
        for x in range(len(games)):
            temp = 0
            if games[x][6] == 'W':
                temp += 1.5
            else:
                temp += .5    

            if (games[x][13] - gamesReverse[x][13]) > 0:
                temp += 1.25
            else:
                temp += .75

            if (games[x][14] - gamesReverse[x][14]) > 0:
                temp += 1.1
            else:
                temp += .9

            if (games[x][15] - gamesReverse[x][15]) > 0:
                temp += 1.15
            else:
                temp += .85

            if (games[x][16] - gamesReverse[x][16]) > 0:
                temp += 1.1
            else:
                temp += .9

            if (games[x][17] - gamesReverse[x][17]) > 0:
                temp += 1.3
            else:
                temp += .7

            calc1 += (temp / 6);

        calc1 = calc1 / len(games)

        # Comparison Between overall stats
        calc2 = (team1Stats[3] / team2Stats[3]) + (team1Stats[10] / team2Stats[10]) + (team1Stats[11] / team2Stats[11]) + (team1Stats[12] / team2Stats[12]) + (team1Stats[13] / team2Stats[13]) + (team1Stats[14] / team2Stats[14])
        calc2 = calc2 / 6

        # Final Calc + Display of choice
        final = ((calc1 * .65) + (calc2 * .35)) * 100

        print("\nGames Comparison Overall: " + str(calc1))
        print("Stats Comparison Overall: " + str(calc2))
        print("\nCombining these two factors...")
        print("Estimated chance of win: " + str(int(final)) + "%\n")
        return
