import mysql.connector

class dbOperations():
    def __init__(self):
        # Establish connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="iarepotato13",
            database="nbaproject"
        )
        print("Database connection established.")

        # Create cursor object
        self.cursor = self.connection.cursor()

    # Deconstructor -- closes cursor and connection
    def destructor(self):
        self.cursor.close()
        self.connection.close()

    # executes a given query
    def executeQuery(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        print("Query Executed.")

    # function for inserting single record
    def insertRecord(self, query, record):
        self.cursor.execute(query,record)
        self.connection.commit()

    # function for bulk inserting records
    def bulkInsert(self,query,record):
        self.cursor.executemany(query,record)
        self.connection.commit()
        print("query executed..")

    # returns records from query
    def getRecords(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    # returns a single record of the table
    def getRecord(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchone()
        return results

    # function to return a single value from table
    def getSingleRecord(self):
        self.cursor.execute()
        return self.cursor.fetchone()[0]