from os import stat
from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.endpoints import leaguegamelog

# Handles processing data from NBA API
class DataGrabber:
    @staticmethod
    def updateDatabase(dbOps):
        DataGrabber.updateTeams(dbOps)
        DataGrabber.updatePlayers(dbOps)
        DataGrabber.updatePlayerStats(dbOps)
        DataGrabber.updateTeamStats(dbOps)

    @staticmethod
    def updatePlayers(dbOps):
        # Grab currently stored Data
        currPlayers = dbOps.getRecords("SELECT playerID FROM player;")

        # Grab new data from API then convert from dict to list
        playerDict = players.get_players() # id, teamID, full_name, first_name, last_name, is_active
        playerList = []
        for player in playerDict:
            temp = list(player.values())
            temp.insert(1, None)
            playerList.append(temp)

        # Compare currData with newData to delete repeats        
        if len(currPlayers) != 0:
            tempList = []
            counter = 0
            for player in playerList:
                for key in currPlayers:
                    if key[0] == player[0]:
                        tempList.append(counter)
                counter = counter + 1
            tempList.reverse()
            for x in tempList:
                playerList.remove(playerList[x])

        # Insert new data into Player Table
        if len(playerList) != 0:
            DataGrabber.insertPlayers(dbOps, playerList)

    @staticmethod
    def insertPlayers(dbOps, pList):
        attribute_count = len(pList[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO player VALUES("+placeholder+")"
        dbOps.bulkInsert(query, pList)
        print(str(len(pList)) + " new players added.")

    @staticmethod
    def updateTeams(dbOps):
        # Grab currently stored Data
        currTeams = dbOps.getRecords("SELECT teamID FROM team;")

        # Grab new data from API then convert from dict to list
        teamDict = teams.get_teams() # id, full_name, abbreviation, nickname, city, state, year_founded
        teamList = []
        for row in teamDict:
            teamList.append(list(row.values()))

        # Compare currData with newData to delete repeats        
        if len(currTeams) != 0:
            tempList = []
            counter = 0
            for team in teamList:
                for key in currTeams:
                    if key[0] == team[0]:
                        tempList.append(counter)
                counter = counter + 1
            tempList.reverse()
            for x in tempList:
                teamList.remove(teamList[x])

        # Insert new data into Team Table
        if len(teamList) != 0:
            DataGrabber.insertTeams(dbOps, teamList)

    @staticmethod
    def insertTeams(dbOps, tList):
        attribute_count = len(tList[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO team VALUES("+placeholder+")"
        dbOps.bulkInsert(query, tList)
        print(str(len(tList)) + " new teams added.")
    
    @staticmethod
    def updatePlayerStats(dbOps):
        # Table formatting + Retrieve data from API
        playerstatsTable = ["playerID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "blocks", "points"]
        pStats = leaguedashplayerstats.LeagueDashPlayerStats().league_dash_player_stats.get_dict()['data']

        # First find player by playerID and add teamID to player table
        for player in pStats:
            query = "UPDATE player SET teamID = %s WHERE playerID = " + str(player[0]) + ";"
            dbOps.executeQuery(query, (player[3],))

        # Only take wanted attributes
        pStatsCleaned = []
        for player in pStats:
            pStatsCleaned.append([player[0], player[7], player[8], player[9], player[11], player[12], player[13], player[14], player[15], player[16], player[22], player[23], player[25], player[26], player[30]])

        # Check if records already exist
        currPlayers = dbOps.getRecords("SELECT playerID FROM playerstats;")
        if len(currPlayers) != 0:
            tempList = []
            counter = 0
            for player in pStatsCleaned:
                for key in currPlayers:
                    if key[0] == player[0]:
                        tempList.append(counter)
                counter = counter + 1
            tempList.reverse()
            for x in tempList:
                pStatsCleaned.remove(pStatsCleaned[x])

        # Then add stats to playerStats table
        if len(pStatsCleaned) != 0:
            DataGrabber.insertPlayerStats(dbOps, pStatsCleaned)

    @staticmethod
    def insertPlayerStats(dbOps, pStats):
        attribute_count = len(pStats[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO playerstats VALUES("+placeholder+");"
        dbOps.bulkInsert(query, pStats)
        print(str(len(pStats)) + " new player's stats added.")

    @staticmethod
    def updateTeamStats(dbOps,):
        # Table formatting + Retrieve data from API
        teamstatsTable = ["teamID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        tStats = leaguedashteamstats.LeagueDashTeamStats().league_dash_team_stats.get_dict()['data']
        
        # Only take wanted attributes
        tStatsCleaned = []
        for team in tStats:
            tStatsCleaned.append([team[0], team[3], team[4], team[5], team[7], team[8], team[9], team[10], team[11], team[12], team[18], team[19], team[21], team[22], team[26]])

        # Check if records already exist
        currTeams = dbOps.getRecords("SELECT teamID FROM teamstats;")
        if len(currTeams) != 0:
            tempList = []
            counter = 0
            for team in tStatsCleaned:
                for key in currTeams:
                    if key[0] == team[0]:
                        tempList.append(counter)
                counter = counter + 1
            tempList.reverse()
            for x in tempList:
                tStatsCleaned.remove(tStatsCleaned[x])

        # Then add tstats to teamstats table
        if len(tStatsCleaned) != 0:
            DataGrabber.insertTeamStats(dbOps, tStatsCleaned)

    @staticmethod
    def insertTeamStats(dbOps, tStats):
        attribute_count = len(tStats[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO teamstats VALUES("+placeholder+");"
        dbOps.bulkInsert(query, tStats)
        print(str(len(tStats)) + " new team's stats added.")

    @staticmethod
    def updateGame(dbOps):
        # Table formatting + Retrieve data from API
        gameTable = ["gameID", "teamID", "matchupteamID", "homeGame", "seasonID", "gameDate", "WL", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        gStats = leaguegamelog.LeagueGameLog().league_game_log.get_dict()['data']
        
        # Only take wanted attributes
        gStatsCleaned = []
        counter = 1
        for game in gStats:
            gStatsCleaned.append([counter, game[1], game[6], None, game[0], game[5], game[7], game[9], game[10], game[11], game[12], game[13], game[14], game[20], game[21], game[22], game[23], game[26]])
            counter = counter + 1

        for game in gStatsCleaned:
            # Fill in home or away
            if game[2].split(" ")[1] == '@':
                game[3] = 0
            else:
                game[3] = 1

            # Convert "matchup" to teamID by search
            query = "SELECT teamID from team WHERE abbreviation LIKE \'%" + game[2].split(" ")[2] + "\';"
            game[2] = dbOps.getRecord(query, None)[0]

        # Check if records already exist
        currGames = dbOps.getRecords("SELECT gameID FROM game;")
        if len(currGames) != 0:
            tempList = []
            counter = 0
            for game in gStatsCleaned:
                for key in currGames:
                    if key[0] == game[0]:
                        tempList.append(counter)
                counter = counter + 1
            tempList.reverse()
            for x in tempList:
                gStatsCleaned.remove(gStatsCleaned[x])

        # Then add tstats to teamstats table
        if len(gStatsCleaned) != 0:
            DataGrabber.insertGame(dbOps, gStatsCleaned)

    @staticmethod
    def insertGame(dbOps, gStats):
        attribute_count = len(gStats[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO game VALUES("+placeholder+");"
        dbOps.bulkInsert(query, gStats)
        print(str(len(gStats)) + " new games added.")
      
        


    