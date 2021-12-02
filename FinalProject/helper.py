# Functions that didnt fit anywhere else

class helper():
    # function prints a list of strings nicely
    @staticmethod
    def prettyPrint(lst):
        for i in lst:
            print(i)
        print("")

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

    # Gets data types from read data
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

    @staticmethod
    def formattedDisplay(attributes, data):
        print()
