import sys

class Person:
    def __init__(self, name, age, area):
        self.name = name
        self.age = age
        self.area = area

class Administrator(Person):
    def __init__(self, name, age, area, department):
        super().__init__(name, age, area)
        self.department = department

class SubChief(Person):
    def __init__(self, name, age, area, department):
        super().__init__(name, age, area)
        self.department = department

class Worker(Person):
    def __init__(self, name, age, area, department):
        super().__init__(name, age, area)
        self.department = department

class PersonnelManager:
    def __init__(self):
        self.personnel = []

    def registerPerson(self, person):
        self.personnel.append(person)

    def displayPersonnel(self):
        for person in self.personnel:
            if isinstance(person, Administrator):
                role = "Administrator"
            elif isinstance(person, SubChief):
                role = "SubChief"
            elif isinstance(person, Worker):
                role = "Worker"
            else:
                role = "Person"
            print(f"Role: {role}")
            print(f"Name: {person.name}")
            print(f"Age: {person.age}")
            print(f"Area: {person.area}")
            if isinstance(person, (Administrator, SubChief, Worker)):
                print(f"Department: {person.department}")
            print("------------")

    def saveToFile(self, filename):
        with open(filename, 'w') as file:
            for person in self.personnel:
                if isinstance(person, Administrator):
                    role = "Administrator"
                elif isinstance(person, SubChief):
                    role = "SubChief"
                elif isinstance(person, Worker):
                    role = "Worker"
                else:
                    role = "Person"
                file.write(f"{role}\n")
                file.write(f"Name: {person.name}\n")
                file.write(f"Age: {person.age}\n")
                file.write(f"Area: {person.area}\n")
                file.write(f"Department: {person.department}\n")
                file.write("------------\n")

    def loadFromFile(self, filename):
        self.personnel = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    role = lines[i].strip()
                    name = lines[i + 1].strip()[6:]
                    age = lines[i + 2].strip()[5:]
                    area = lines[i + 3].strip()[6:]
                    department = lines[i + 4].strip()[12:]
                    if role == "Administrator":
                        person = Administrator(name, age, area, department)
                    elif role == "SubChief":
                        person = SubChief(name, age, area, department)
                    elif role == "Worker":
                        person = Worker(name, age, area, department)
                    else:
                        person = Person(name, age, area)
                    self.personnel.append(person)
                    i += 6
        except FileNotFoundError:
            print("File not found.")

def main():
    manager = PersonnelManager()

    while True:
        print("====================================")
        print("            Main Menu")
        print("====================================")
        print(" 0. Exit")
        print(" 1. Register Administrator")
        print(" 2. Register SubChief")
        print(" 3. Register Worker")
        print(" 4. Display Personnel")
        print(" 5. Save to File")
        print(" 6. Load from File")
        print("====================================")
        option = input("Enter your option: ")

        if option == "0":
            sys.exit()
        elif option == "1":
            name = input("Enter Administrator's name: ")
            age = input("Enter Administrator's age: ")
            area = input("Enter Administrator's area: ")
            department = input("Enter Administrator's department: ")
            admin = Administrator(name, age, area, department)
            manager.registerPerson(admin)
        elif option == "2":
            name = input("Enter SubChief's name: ")
            age = input("Enter SubChief's age: ")
            area = input("Enter SubChief's area: ")
            department = input("Enter SubChief's department: ")
            subchief = SubChief(name, age, area, department)
            manager.registerPerson(subchief)
        elif option == "3":
            name = input("Enter Worker's name: ")
            age = input("Enter Worker's age: ")
            area = input("Enter Worker's area: ")
            department = input("Enter Worker's department: ")
            worker = Worker(name, age, area, department)
            manager.registerPerson(worker)
        elif option == "4":
            manager.displayPersonnel()
        elif option == "5":
            filename = input("Enter the filename to save to: ")
            manager.saveToFile(filename)
        elif option == "6":
            filename = input("Enter the filename to load from: ")
            manager.loadFromFile(filename)
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
