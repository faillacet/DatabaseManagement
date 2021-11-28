from DataGrabber import DataGrabber
from dbOperations import dbOperations
from helper import helper

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
    dbOps = dbOperations()
    DataGrabber.updateDatabase(dbOps)
    #DataGrabber.tester()

    print("Done :)")
    # getTeamList()
    # gameInfo = teamgamelog.TeamGameLog(tempID)
    # print(gameInfo.get_normalized_json())
    
# ------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()