from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import teamdashboardbyteamperformance
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import leaguedashplayerstats

# Handles processing data from NBA API
class DataGrabber:
    @staticmethod
    def updateDatabase(dbOps):
        DataGrabber.updateTeams(dbOps)
        DataGrabber.updatePlayers(dbOps)
        DataGrabber.updatePlayerStats(dbOps)

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
        # Retrieve player stats from API --- FORMAT
        playerStatsAPIAttr = ["PLAYER_ID", "PLAYER_NAME", "PLAYER_FIRST_NAME", "TEAM_ID", "TEAM_ABBREVIATION", "AGE", "GP", "W", "L", "W_PCT",
                            "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT", "OREB",
                            "DREB", "REB", "AST", "TOV", "STL", "BLK", "BLKA", "PF", "PFD", "PTS", "PLUS_MINUS", "NBA_FANTASY_PTS",
                            "DD2", "TD3", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK",
                            "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK",
                            "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK",
                            "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "CFID", "CFPARAMS"]
        playerStatsAttr = ["playerID", "W", "L", "W_PCT", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "REB", "AST", "BLK"]

        # First find player by playerID and add teamID to player table
        pStats = leaguedashplayerstats.LeagueDashPlayerStats().league_dash_player_stats.get_dict()['data']
        for player in pStats:
            query = "UPDATE player SET teamID = %s WHERE playerID = " + str(player[0]) + ";"
            dbOps.executeQuery(query, (player[3],))

        # Then add stats to playerStats table
        pStats = []
        attribute_count = len(pStats[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        for player in pStats:
            query = "INSERT INTO playerstats VALUES("+placeholder+");"


    @staticmethod
    def getTeamStats(dbOps, tID):
        # Retrieve team stats from API
        try:
            tInfo = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=tID).overall_team_dashboard.get_dict()
            tInfo = tInfo['data'][0]
            # ID, TimeFrame, Wins, Losses, WinPCT, FG_PCT, FG3_PCT, REB, AST, BLK, PTS
            tInfo = [tID, "2021-22", tInfo[3], tInfo[4], tInfo[5], tInfo[9], tInfo[12], tInfo[18], tInfo[19], tInfo[22], tInfo[26]]
        except:
            return False
        # Insert into database
        attrCount = len(tInfo)
        placeHolder = ("%s,"*attrCount)[:-1]
        query = "INSERT INTO teamstats VALUES("+placeHolder+")"
        dbOps.insertRecord(query, tInfo)
        return True

    @staticmethod
    def getGame(dbOps, tID):
        attr = ["teamID", "gameID", "gameDate", "matchup", "WL", "W", "L", "W_PCT", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT",
                "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
        attrKeep = ["gameID", "teamID", "gameDate", "matchup", "WL", "wPCT", "fgPCT", "fg3PCT", ""]
        gInfo = teamgamelog.TeamGameLog(team_id=1610612737).get_dict()
        gInfo = gInfo['resultSets'][0]['rowSet']
        for x in gInfo:
            print(x)
        


        

        
 