# Database Management Final

* Trenton Faillace

# NBA Metrics

* Project implemented in python with MySQL backend
* Uses python nba 

# Dependencies

* https://github.com/swar/nba_api
* Quick install: pip install nba_api
* I think you also need numpy, but you probably already have this

# Instructions

* Simply compile main.py with python3 (python3 main.py)
* Probably dont want to update Database, on the cloud it takes WAY too long, but my pc can handle it fine
* Public IP: 34.133.182.114, user: root, password: 1444password, database: nbaproject

# Notes - Where to Find requirements

* Display Records - DisplayData.py
* Query Data - QueryData.py
* Create records - AddRecords.py
* Delete Records (no soft delete) - DeleteRecords.py 
* Update Records - UpdateRecords.py
* Transactions - Under DeleteRecors.py in deletePlayer() and deleteTeam()
* Reports - in Export.py
* Group-by clause - QueryData.py statsByState()
* Sub-query - QueryData.py chanceToWin()
* Joins across 3 tables - QueryData.py gameBetweenTwoTeams() and gamesBetweenTwoPlayers()
* Referential integrity - Mostly in DataGrabber.py and DeleteRecords.py
* Views and Indexes - in SQLStuff.txt as well as implemented in DisplayData.py teamData()

# Other Notes

* I wasnt entirely sure what you meant by generate reports, so I simply allowed the tables to be printed to csv format\

