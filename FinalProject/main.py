from dbOperations import dbOperations
from helper import helper
from nba_api.stats.static import teams
from nba_api.stats.static import players
# FOR SURE USING ^
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import teamgamelog

# GLOBALS ----------------------------------------------
nbaCode = 00
tempID = 1610612737
# ------------------------------------------------------

def getTeamList():
    teamList = teams.get_teams()
    helper.prettyPrint(teamList)

def getTeamInfo(id):
    teamInfo = teaminfocommon.TeamInfoCommon(id)
    print(teamInfo.get_normalized_dict())


# Main Function ----------------------------------------
def main():
    # getTeamList()
    # gameInfo = teamgamelog.TeamGameLog(tempID)
    # print(gameInfo.get_normalized_json())
    dbops = dbOperations()
# ------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()