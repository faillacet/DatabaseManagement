from helper import helper

class AddRecords:
    @staticmethod
    def addPlayer(dbOps):
        attr = ["pID (int)", "Full Name (string)", "First Name (string)", "Last Name (string)", "isActive (bool- 0 or 1)"]
        print("-----NOTE: Enter \"NULL\" if the value DNE-----")
        print("Please fill in all the following values to insert into table player:")
        record = []

        for x in attr:
            if x == "pID (int)":
                # Check to see if ID already exists in DB
                query = "SELECT playerID FROM player WHERE playerID = %s"
                while True:
                    id = input(x +": ")
                    if dbOps.getRecord(query, (id,)) != None:
                        print("\nA record with this ID already exists, try again...\n")
                    else:
                        record.append(id)
                        break
            else:
                record.append(input(x +": "))

        # Insert Record
        try:
            attrCount = len(record)
            placeholder = ("%s,"*attrCount)[:-1]
            query = "INSERT INTO player VALUES("+placeholder+");"
            dbOps.insertRecord(query, tuple(record))
            print("Player Successfully Inserted! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")
        
        return
        
    @staticmethod
    def addPlayerStats(dbOps):
        attr = ["pID (int)", "timeFrame (string)", "PTS (float)", "AST (float)", "REB (float)", "PIE (float)"]
        print("-----NOTE: Enter \"NULL\" if the value DNE-----")
        print("-----NOTE: A Player with same ID must already exist in player table-----")
        print("-----NOTE: Type \"quit\" to return to menu-----")
        print("Please fill in all the following values to insert into table playerstats:")
        record = []

        for x in attr:
            if x == "pID (int)":
                # Check to see if ID already exists in DB
                query = "SELECT playerID FROM playerstats WHERE playerID = %s;"
                # Check to see if ID already exists in player table
                query2 = "SELECT playerID FROM player WHERE playerID = %s;"
                while True:
                    id = input(x +": ")
                    if id == "quit":
                        return
                    elif dbOps.getRecord(query, (id,)) != None:
                        print("\nA record with this ID already exists, try again...\n")
                    elif dbOps.getRecord(query2, (id,)) == None:
                        print("\nA record with this ID DNE within player table, try again...\n")
                    else:
                        record.append(id)
                        break
            else:
                uInput = input(x +": ")
                if uInput == "quit":
                    return
                record.append(uInput)

        # Insert Record
        try:
            attrCount = len(record)
            placeholder = ("%s,"*attrCount)[:-1]
            query = "INSERT INTO playerstats VALUES("+placeholder+");"
            dbOps.insertRecord(query, tuple(record))
            print("Playerstats Successfully Inserted! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")

        return

    @staticmethod
    def addTeam(dbOps):
        attr = ["teamID (int)", "Name (string)", "Abbreviation (string)", "Nickname (string)", "City (string)", "State (string)", "YearFounded (int)"]
        print("-----NOTE: Enter \"NULL\" if the value DNE-----")
        print("Please fill in all the following values to insert into table team:")
        record = []

        for x in attr:
            if x == "teamID (int)":
                # Check to see if ID already exists in DB
                query = "SELECT teamID FROM team WHERE teamID = %s"
                while True:
                    id = input(x +": ")
                    if dbOps.getRecord(query, (id,)) != None:
                        print("\nA record with this ID already exists, try again...\n")
                    else:
                        record.append(id)
                        break
            else:
                record.append(input(x +": "))

        # Insert Record
        try:
            attrCount = len(record)
            placeholder = ("%s,"*attrCount)[:-1]
            query = "INSERT INTO team VALUES("+placeholder+");"
            dbOps.insertRecord(query, tuple(record))
            print("Team Successfully Inserted! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")

        return
            
    @staticmethod
    def addTeamStats(dbOps):
        attr = ["pID", "TimeFrame", "Wins", "Losses", "WinPCT", "FG_PCT", "FG3_PCT", "REB", "AST", "BLK", "PTS"]
        print("-----NOTE: Enter \"NULL\" if the value DNE-----")
        print("-----NOTE: A Player with same ID must already exist in player table-----")
        print("-----NOTE: Type \"quit\" to return to menu-----")
        print("Please fill in all the following values to insert into table team:")
        record = []

        for x in attr:
            if x == "pID":
                # Check to see if ID already exists in DB
                query = "SELECT teamID FROM teamstats WHERE teamID = %s"
                # Check to see if ID already exists in team table
                query2 = "SELECT teamID FROM team WHERE teamID = %s"
                while True:
                    id = input(x +": ")
                    if id == "quit":
                        return
                    elif dbOps.getRecord(query, (id,)) != None:
                        print("\nA record with this ID already exists, try again...\n")
                    elif dbOps.getRecord(query2, (id,)) == None:
                        print("\nA record with this ID DNE within team table, try again...\n")
                    else:
                        record.append(id)
                        break
            else:
                record.append(input(x +": "))

        # Insert Record
        try:
            attrCount = len(record)
            placeholder = ("%s,"*attrCount)[:-1]
            query = "INSERT INTO teamstats VALUES("+placeholder+");"
            dbOps.insertRecord(query, tuple(record))
            print("Teamstats Successfully Inserted! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")

        return

    @staticmethod
    def addGame(dbOps):
        print()
