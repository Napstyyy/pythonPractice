import sys
class User:
    # Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


#Product class definition
class Product:
    def __init__(self, _name, _amount) -> None:
        self.name = _name
        self.amount = _amount

    def register(self):
        with open("stock.txt", "a") as file:
            file.write(f"Name: {self.name}\nAmount: {self.amount}\n -----------------------------------------------------\n")
            file.close

class Main:
    # Constructor
    def __init__(self):
        file = open("users.txt", "w")
        file.close
        pass

    # Kind of Destructor
    def kill(self):
        sys.exit()