# Class that manages parsing the data into correct tables
# Handles the ID management as well

class DataParser:
    # function parses a string and converts to appropriate type
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    # initial parse of data from file
    @staticmethod
    def parseFile(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()

        data = [i.strip().split(",") for i in data]
        data_cleaned = []
        for row in data[:]:
            row = [DataParser.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned

    # creates data for agency table
    @staticmethod
    def agencySort(initData, list):
        # agency Stores (agencyID, Name, Origin)
        for row in initData:
            if [None, row[6], row[7]] not in list:
                list.append([None, row[6], row[7]])
        list.pop(0)

        # Assign ID to each
        index = 1
        for row in list:
            row[0] = index
            index = index + 1
            
    @staticmethod
    def astronautSort(initData, agencyList, list):
        # astronaut Stores (astronautID, Name, Age, Agency(ID))
        for row in initData:
            if [None, row[1], row[2], row[6]] not in list:
                list.append([None, row[1], row[2], row[6]])
        list.pop(0)

        # Assign ID to each
        index = 1
        for row in list:
            row[0] = index
            index = index + 1

        # Set up foreign key to AgencyID
        for astronaut in list:
            for agency in agencyList:
                if astronaut[3] == agency[1]:
                    astronaut[3] = agency[0]

    @staticmethod
    def expeditionSort(initData, list):
        # expedition Stores (expeditionNumber, Duration)
        for row in initData:
            if [row[0], row[5]] not in list:
                list.append([row[0], row[5]])
        list.pop(0)

    @staticmethod
    def astroexpSort(initData, astroList, list):
        # astro_expedition Stores (ID, Expedition(ID), Astronaut(ID))
        for row in initData:
            list.append([None, row[0], row[1]])
        list.pop(0)

        # list is currently stored as [None, ExpID, Astronaut Name]
        # Convert to [None, ExpID, AstroID]
        for row in list:
            for astro in astroList:
                if row[2] == astro[1]:
                    row[2] = astro[0]

        # Generate IDs
        index = 1
        for row in list:
            row[0] = index
            index = index + 1