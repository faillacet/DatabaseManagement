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
            while len(playerList) != 0:
                chunk = []
                counter = 0
                while counter < 100 and len(playerList) != 0:
                    chunk.append(playerList[counter])
                    counter = counter + 1
                DataGrabber.insertPlayers(dbOps, chunk)
                while counter != -1:
                    playerList.pop(0)
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