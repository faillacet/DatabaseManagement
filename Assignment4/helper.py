# module contains miscellaneous functions

class helper():
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

    # function reads file path to clean up data file
    @staticmethod
    def data_cleaner(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()

        data = [i.strip().split(",") for i in data]
        data_cleaned = []
        for row in data[:]:
            row = [helper.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned

    # function checks for user input given a list of choices
    @staticmethod
    def get_choice(lst):
        choice = input("Enter choice number: ")
        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")
        return int(choice)

    # function prints a list of strings nicely
    @staticmethod
    def pretty_print(lst):
        print("Results..")
        for i in lst:
            print(i)
        print("")

    @staticmethod
    def songsPrint(lst):
        print("Values for given song:")
        print("Song ID: ", end='')
        print(lst[0])
        print("Song Name: ", end='')
        print(lst[1])
        print("Artist: ", end='')
        print(lst[2])
        print("Album: ", end='')
        print(lst[3])
        print("Release Date: ", end='')
        print(lst[4])
        print("Genre: ", end='')
        print(lst[5])
        print("Explicit: ", end='')
        print(lst[6])
        print("Duration: ", end='')
        print(lst[7])
        print("Energy: ", end='')
        print(lst[8])
        print("Daceability: ", end='')
        print(lst[9])
        print("Acousticness: ", end='')
        print(lst[10])
        print("Liveness: ", end='')
        print(lst[11])
        print("Loudness: ", end='')
        print(lst[12])

    @staticmethod
    def containsNumber(value):
        for character in value:
            if character.isdigit():
                return True
        return False