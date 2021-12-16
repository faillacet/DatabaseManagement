from helper import helper

class QueryData:
    @staticmethod
    def displayTop10(dbOps):
        print("Display:\n1) Top 10 Players \n2) Top 10 Teams")
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
    def statsByState(dbOps):
        # Method to view the average stats for teams by the state they are based in
        print("This feature shows the average stats for teams per state...")

        # Gets stats by state
        query = '''SELECT state, avg(points), avg(wins), avg(losses), avg(rebounds), avg(assists), avg(steals), avg(blocks) 
                FROM teamstats as tStats
                NATURAL JOIN (SELECT teamID, state FROM team) as team
                GROUP BY state; '''
        stats = dbOps.getRecords(query)
        
        print()
        for city in stats:
            print(city[0] + ": ")
            print("Points: " + str(city[1]))
            print("Wins: " + str(city[2]))
            print("Losses: " + str(city[3]))
            print("Rebounds: " + str(city[4]))
            print("Assists: " + str(city[5]))
            print("Steals: " + str(city[6]))
            print("Blocks: " + str(city[7]) + "\n")

        return

    @staticmethod
    def gamesBetweenTwoPlayers(dbOps):
        # Calcs how many games are played between two players
        print("This feature will calculate how many games are played between two players.")
        name = input("Enter Full Name of player1: ")
        name2 = input("Enter Full Name of player2: ")
        names = [name, name2]

        query = '''SELECT count(*)
                FROM game as g
                INNER JOIN (SELECT teamID FROM player Where fullName = %s) as p1
                ON g.teamID = p1.teamID
                INNER JOIN (SELECT teamID FROM player WHERE fullName = %s) as p2
                ON g.matchupteamID = p2.teamID;
                '''
        result = dbOps.getRecord(query, names)
        print("\n Number of games played: " + str(result[0]))
        print()
        return

    @staticmethod
    def gameBetweenTwoTeams(dbOps):
        # Calcs games between two teams by name
        print("This feature will caclulate how many games are played between two teams.")
        name = input("Enter Team Name 1: ")
        name2 = input("Enter Team Name 2: ")
        names = [name, name2]

        query = '''SELECT count(*)
                FROM game as g
                INNER JOIN (SELECT teamID FROM team Where name = %s) as t1
                ON g.teamID = t1.teamID
                INNER JOIN (SELECT teamID FROM team WHERE name = %s) as t2
                ON g.matchupteamID = t2.teamID;
                '''

        result = dbOps.getRecord(query, names)
        print("\n Number of games played: " + str(result[0]))
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
                temp += 5
            else:
                temp -= 5

            if (games[x][13] > gamesReverse[x][13]):
                temp += 2
            else:
                temp -= 2

            if (games[x][14] > gamesReverse[x][14]):
                temp += 2
            else:
                temp -= 2

            if (games[x][15] > gamesReverse[x][15]):
                temp += 1
            else:
                temp -= 1

            if (games[x][16] > gamesReverse[x][16]):
                temp += 1
            else:
                temp -= 1

            if (games[x][17] > gamesReverse[x][17]):
                temp += 2.5
            else:
                temp -= 2.5

            calc1 += temp

        calc1 = calc1 / len(games)

        # Comparison Between overall stats
        calc2 = 0
        if team1Stats[3] > team2Stats[3]:
            calc2 += 5
        else:
            calc2 -= 5

        if team1Stats[10] > team2Stats[10]:
            calc2 += 1
        else:
            calc2 -= 1

        if team1Stats[11] > team2Stats[11]:
            calc2 += 1
        else:
            calc2 -= 1

        if team1Stats[12] > team2Stats[12]:
            calc2 += 1
        else:
            calc2 -= 1

        if team1Stats[13] > team2Stats[13]:
            calc2 += 1
        else:
            calc2 -= 1

        if team1Stats[14] > team2Stats[14]:
            calc2 += 3
        else:
            calc2 -= 3

        calc2 = calc2 / 6

        # Final Calc + Display of choice
        final = (50 + ((calc1 * .55) + (calc2 * .45)))

        print("\nGames Comparison Overall: " + str(calc1))
        print("Stats Comparison Overall: " + str(calc2))
        print("\nCombining these two factors...")
        print("Estimated chance of win: " + str(int(final)) + "%\n")
        return
