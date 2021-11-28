# module defines operations to use with sqlite3 database
import sqlite3


class db_operations():
    def __init__(self,conn_path): # constructor with connection path to db
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("connection made..")

    # function for bulk inserting records
    def bulk_insert(self,query,records):
        self.cursor.executemany(query,records)
        self.connection.commit()
        print("query executed..")

    # function for updating records (chaning a value)
    def changeRecord(self,query):
        self.cursor.execute(query)
        print("Record sucessfully updated...")

    # function to delete a given record
    def deleteRecord(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # function to delete a given record + dictionary input
    def deleteRecordDictionary(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    # function to return a single value from table
    def single_record(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def wholeRecord(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def wholeRecordDictionary(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        resutls = self.cursor.fetchall()
        return resutls

    # function to return a single attribute values from table
    def single_attribute(self,query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results

    # SELECT with named placeholders
    def name_placeholder_query(self,query,dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results

    # close connection 
    def destructor(self):
        self.connection.close()
