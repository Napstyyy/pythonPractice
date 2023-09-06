import sys
class User:
    # Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Main:
    # Constructor
    def __init__(self):
        file = open("users.txt", "w")
        file.close
        pass

    # Kind of Destructor
    def kill(self):
        sys.exit()
    
    # Saving users into a txt file
    def CreateUser(self):
        name = str(input("Enter a username: "))
        age = int(input("Enter the user age: "))
        gender = str(input("Enter a gender: "))
        user = User(name, age, gender)
        with open("users.txt", "a") as file:
            file.write(f"Username: {user.name}\nAge: {user.age}\nGender: {user.gender}\n -----------------------------------------------------\n")
            file.close
    
    # Checking txt file
    def CheckUsers(self):
        print('')
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            file.close
            username = ""
            age = ""
            gender = ""
            for line in lines:
                if line.startswith("Username:"):
                    # Extract the username from the line
                    username = line[len("Username:"):].strip()
                elif line.startswith("Age:"):
                    # Extract the age from the line
                    age = line[len("Age:"):].strip()
                elif line.startswith("Gender:"):
                    # Extract the age from the line
                    gender = line[len("Gender:"):].strip()
                elif line.strip() == "-----------------------------------------------------":
                    if username and age:
                        print(f"Username: {username}")
                        print(f"Age: {age}")
                        print(f"Gender: {gender}")
                        print("-----------------------------------------------------")

                    # Reset variables for the next user
                    username = ""
                    age = ""
                    gender = ""
    
    # Edit user information
    def editUserInfo(self):
        # Ask the user for input
        usernameToUpdate = input("Enter the username to update: ")
        newAge = input("Enter the new age: ")
        newGender = input("Enter the new gender: ")

        # Open the file in read mode
        with open('users.txt', 'r') as file:
            lines = file.readlines()

        # Initialize variables to track user data
        userStart = None
        userEnd = None

        # Find the user's information and record its position
        for i, line in enumerate(lines):
            if line.startswith("Username: " + usernameToUpdate):
                userStart = i
                break

        if userStart is not None:
            for i in range(userStart, len(lines)):
                if lines[i].startswith(" -----------------------------------------------------"):
                    userEnd = i
                    break

        # If the user is found, update their age and gender
        if userStart is not None and userEnd is not None:
            lines[userStart + 1] = f"Age: {newAge}\n"
            lines[userStart + 2] = f"Gender: {newGender}\n"

            # Open the file in write mode and write the updated content
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            print(f"User '{usernameToUpdate}' updated successfully.")
        else:
            print(f"User '{usernameToUpdate}' not found.")

    # Delete user information
    def deleteUser(self):
        # Ask the user for input
        usernameToDelete = input("Enter the username to delete: ")

        # Open the file in read mode
        with open('users.txt', 'r') as file:
            lines = file.readlines()

        # Initialize variables to track user data
        userStart = None
        userEnd = None

        # Find the user's information and record its position
        for i, line in enumerate(lines):
            if line.startswith("Username: " + usernameToDelete):
                userStart = i
                break

        if userStart is not None:
            for i in range(userStart, len(lines)):
                if lines[i].startswith(" -----------------------------------------------------"):
                    userEnd = i
                    break

        # If the user is found, delete their information
        if userStart is not None and userEnd is not None:
            del lines[userStart:userEnd + 1]

            # Open the file in write mode and write the updated content
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            print(f"User '{usernameToDelete}' deleted successfully.")
        else:
            print(f"User '{usernameToDelete}' not found.")


    def main(self):
        while True:
            print("====================================")
            print("            Main Menu")
            print("====================================")
            print(" 0. Exit")
            print(" 1. Create a user")
            print(" 2. Check users")
            print(" 3. Edit a user")
            print(" 4. Delete User")
            print("====================================")            
            option = int(input("Enter your option: "))
            match option:
                case 0:
                    self.kill()
                case 1:
                    print("\n")
                    self.CreateUser()
                case 2:
                    print("\n")
                    self.CheckUsers()
                case 3:
                    print("\n")
                    self.editUserInfo()
                case 4:
                    print("\n")
                    self.deleteUser()
                case _:
                    print("Invalid option")
            print("\n")

init = Main()
init.main()
