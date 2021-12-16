class AddRecords:
    @staticmethod
    def addPlayer(dbOps):
        attr = ["pID (int)", "teamID (int)", "Full Name (string)", "First Name (string)", "Last Name (string)", "isActive (bool- 0 or 1)"]
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
        attr = ["playerID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "blocks", "points"]
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
        attr = ["teamID", "wins", "losses", "winPCT", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
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
        attr = ["gameID", "teamID", "matchupteamID", "homeGame", "seasonID", "gameDate", "WL", "fgM", "fgA", "fgPCT", "fg3M", "fg3A", "fg3PCT", "rebounds", "assists", "steals", "blocks", "points"]
        print("-----NOTE: Enter \"NULL\" if the value DNE-----")
        print("-----NOTE: A Team with same teamID/matchupID must already exist in team table-----")
        print("-----NOTE: Type \"quit\" to return to menu-----")
        print("Please fill in all the following values to insert into game table:")
        record = []

        for x in attr:
            if x == "gameID":
                query = "SELECT gameID FROM game where gameID = %s;"
                while True:
                    id = input(x +": ")
                    if id == "quit":
                        return
                    elif dbOps.getRecord(query, (id,)) != None:
                        print("\nA record with this gameID already exists, try again...\n")
                    else:
                        record.append(id)
                        break
            elif x == "teamID" or x == "matchupteamID":
                # Check to see if ID already exists in DB
                query = "SELECT teamID FROM team WHERE teamID = %s"
                while True:
                    id = input(x +": ")
                    if id == "quit":
                        return
                    elif dbOps.getRecord(query, (id,)) == None:
                        print("\nA record with this ID DNE, try again...\n")
                    else:
                        record.append(id)
                        break
            else:
                record.append(input(x +": "))

        # Insert Record
        try:
            attrCount = len(record)
            placeholder = ("%s,"*attrCount)[:-1]
            query = "INSERT INTO game VALUES("+placeholder+");"
            dbOps.insertRecord(query, tuple(record))
            print("Game Successfully Inserted! \nReturning to menu...\n")
        except:
            print("Error parsing values, formatting not correct...")

        return