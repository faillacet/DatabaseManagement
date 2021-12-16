import csv
import os

class Export:
    @staticmethod
    def export(dbOps):
        # Player table ------------------------------------------------------------------------------------
        query = "SELECT * FROM player;"
        players = dbOps.getRecords(query)

        # Check if FIle exists, if not create
        if not os.path.exists("player.csv"):
            open("player.csv", "w+").close()

        # Write to file
        with open('player.csv', "w+", newline='') as playerFile:
            playerWriter = csv.writer(playerFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for player in players:
                playerWriter.writerow(player)

        # Team table ------------------------------------------------------------------------------------
        query = "SELECT * FROM team;"
        teams = dbOps.getRecords(query)

        # Check if FIle exists, if not create
        if not os.path.exists("team.csv"):
            open("team.csv", "w+").close()

        # Write to file
        with open('team.csv', "w+", newline='') as teamFile:
            teamWriter = csv.writer(teamFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for team in teams:
                teamWriter.writerow(team)

        # player stats table ------------------------------------------------------------------------------------
        query = "SELECT * FROM playerstats;"
        playerstats = dbOps.getRecords(query)

        # Check if FIle exists, if not create
        if not os.path.exists("playerstats.csv"):
            open("playerstats.csv", "w+").close()

        # Write to file
        with open('playerstats.csv', "w+", newline='') as playerstatsFile:
            playerstatsWriter = csv.writer(playerstatsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for player in playerstats:
                playerstatsWriter.writerow(player)

        # team stats table ------------------------------------------------------------------------------------
        query = "SELECT * FROM teamstats;"
        teamstats = dbOps.getRecords(query)

        # Check if FIle exists, if not create
        if not os.path.exists("teamstats.csv"):
            open("teamstats.csv", "w+").close()

        # Write to file
        with open('teamstats.csv', "w+", newline='') as teamstatsFile:
            teamstatsWriter = csv.writer(teamstatsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for team in teamstats:
                teamstatsWriter.writerow(team)

        # game table ------------------------------------------------------------------------------------
        query = "SELECT * FROM game;"
        games = dbOps.getRecords(query)

        # Check if FIle exists, if not create
        if not os.path.exists("game.csv"):
            open("game.csv", "w+").close()

        # Write to file
        with open('game.csv', "w+", newline='') as gameFile:
            gameWriter = csv.writer(gameFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for game in games:
                gameWriter.writerow(game)
