# Program Entry point
from dbOperations import dbOperations
from helper import helper
from DataParser import DataParser

def isEmpty(dbOps):
    query = "SELECT COUNT(*) FROM agency;"
    result = dbOps.getSingleRecord(query)
    return result == 0

def fillAgency(dbOps, records):
    attribute_count = len(records[0])
    placeholders = ("%s,"*attribute_count)[:-1]
    query = "INSERT INTO agency VALUES("+placeholders+")"
    dbOps.bulkInsert(query, tuple(records)) 

def fillAstro(dbOps, records):
    attribute_count = len(records[0])
    placeholders = ("%s,"*attribute_count)[:-1]
    query = "INSERT INTO astronaut VALUES("+placeholders+")"
    dbOps.bulkInsert(query, tuple(records)) 

def fillExpedition(dbOps, records):
    attribute_count = len(records[0])
    placeholders = ("%s,"*attribute_count)[:-1]
    query = "INSERT INTO expedition VALUES("+placeholders+")"
    dbOps.bulkInsert(query, tuple(records)) 

def fillAstroExp(dbOps, records):
    attribute_count = len(records[0])
    placeholders = ("%s,"*attribute_count)[:-1]
    query = "INSERT INTO astro_expedition VALUES("+placeholders+")"
    dbOps.bulkInsert(query, tuple(records)) 


# Main program
def main():
    # Establish connection to DB
    dbOps = dbOperations()

    # Handle data from expeditionData.csv -----------------------------
    initData = DataParser.parseFile("expeditionData.csv") 

    agencyData = []
    DataParser.agencySort(initData, agencyData)

    astronautData = []
    DataParser.astronautSort(initData, agencyData, astronautData)

    expeditionData = []
    DataParser.expeditionSort(initData, expeditionData)

    astroexpData = []
    DataParser.astroexpSort(initData, astronautData, astroexpData)
    # -----------------------------------------------------------------

    # TESTING PURPOSES
    # dbOps.executeQuery("DELETE FROM astro_expedition;")
    # dbOps.executeQuery("DELETE FROM expedition;")
    # dbOps.executeQuery("DELETE FROM astronaut;")
    # dbOps.executeQuery("DELETE FROM agency;")

    # Data has been parsed, now we push to database -------------------
    if isEmpty(dbOps):
        fillAgency(dbOps, agencyData)
        fillAstro(dbOps, astronautData)
        fillExpedition(dbOps, expeditionData)
        fillAstroExp(dbOps, astroexpData)
        print()
    else:
        # If the data has been previously inserted, Displays data in the database
        print("Data already exists... Printing Tables:")
        print("Agency:")
        result = dbOps.getRecords("SELECT * FROM agency;")
        helper.pretty_print(result)

        print("Astronaut:")
        result = dbOps.getRecords("SELECT * FROM astronaut;")
        helper.pretty_print(result)

        print("Expedition:")
        result = dbOps.getRecords("SELECT * FROM expedition;")
        helper.pretty_print(result)

        print("Astro_Expedition:")
        result = dbOps.getRecords("SELECT * FROM astro_expedition;")
        helper.pretty_print(result)

    # -----------------------------------------------------------------

# Ensures main is called when file is run
if __name__ == "__main__":
    main()