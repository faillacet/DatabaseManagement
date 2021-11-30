from os import stat
from nba_api.stats import static
from helper import helper
from dbOperations import dbOperations
from nba_api.stats.static import teams
from nba_api.stats.static import players

from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import teamgamelog

# Handles processing data from NBA API
class DataGrabber:
    @staticmethod
    def updateDatabase(dbOps):
        DataGrabber.updatePlayers(dbOps)
        DataGrabber.updateTeams(dbOps)

    @staticmethod
    def updatePlayers(dbOps):
        # Grab currently stored Data
        currPlayers = dbOps.getRecords("SELECT playerID FROM player;")

        # Grab new data from API then convert from dict to list
        playerDict = players.get_players() # id, full_name, first_name, last_name, is_active
        playerList = []
        for row in playerDict:
            playerList.append(list(row.values()))

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
    def tester(dbOps):
        pID = 555555
        # Grab new data from API then convert from dict to list
        try:
            playerInfo = commonplayerinfo.CommonPlayerInfo(player_id=pID).player_headline_stats.get_dict()
            print(playerInfo['data'][0])
        except:
            print("Some error occured...")

    
    @staticmethod
    def getPlayerStats(dbOps, pID):
        # Retrieve player stats from API
        # pID, name, timeframe, pts, ast, reb, pie
        try:
            playerInfo = commonplayerinfo.CommonPlayerInfo(player_id=pID).player_headline_stats.get_dict()
            stats = playerInfo['data'][0]
            stats.pop(1)
            print(stats)

            # Insert into database
            attribute_count = len(stats)
            placeholder = ("%s,"*attribute_count)[:-1]
            query = "INSERT INTO playerstats VALUES("+placeholder+")"
            dbOps.insertRecord(query, stats)
            return True;
        except:
            return False;



        

        
 