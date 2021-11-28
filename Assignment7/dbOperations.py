import mysql.connector

class dbOperations():
    def __init__(self):
        # Establish connection
        self.connection = mysql.connector.connect(
            host="34.133.182.114",
            user="rao",
            password="password1",
            database="cpsc408"
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

    # function for bulk inserting records
    def bulkInsert(self,query,record):
        self.cursor.executemany(query,record)
        self.connection.commit()
        print("query executed..")

    # returns a single record of the table
    def getRecords(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results    

    # function to return a single value from table
    def getSingleRecord(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]