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
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    @staticmethod
    def updateDatabase(dbOps):
        # Grab currently stored Data
        currPlayers = dbOps.getRecords("SELECT playerID FROM player;")
        #currTeams = dbOps.getRecords("")

        # Grab new data from API then convert from dict to list
        # Player
        playerDict = players.get_players() # id, full_name, first_name, last_name, is_active
        playerList = []
        for row in playerDict:
            playerList.append(list(row.values()))

        # Team
        teamDict = teams.get_teams() # id, full_name, abbreviation, nickname, city, state, year_founded
        teamList = []
        for row in teamDict:
            teamList.append(list(row.values()))

        # Compare currData with newData to delete repeats
        # Player
        newPlayers = []
        if len(currPlayers) != 0:
            for player in playerList:
                for id in currPlayers:
                    if id != player[0]:
                        newPlayers.append(player)
        else:
            for player in playerList:
                newPlayers.append(player)
        
        # Team

        # Insert new data into database
        # Player Table
        if len(newPlayers) != 0:
            
            DataGrabber.insertPlayers(dbOps, newPlayers)
            DataGrabber.tester()
        # Team Table


    @staticmethod
    def insertPlayers(dbOps, pList):
        attribute_count = len(pList[0])
        placeholder = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO player VALUES("+placeholder+")"
        dbOps.bulkInsert(query, pList)
        print(str(len(pList)) + " new players added.")
        
    @staticmethod
    def tester():
        print("")