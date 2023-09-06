import sys
class Product:
    # Constructor
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Main:
    # Constructor
    def __init__(self):
        file = open("Inventory.txt", "w")
        file.close
        pass

    # Kind of Destructor
    def kill(self):
        sys.exit()
    
    # Saving users into a txt file
    def AddNewElement(self):
        name = str(input("Enter the product's name: "))
        stock = int(input("Enter the product's stock "))
        product = Product(name, stock)
        with open("Inventory.txt", "a") as file:
            file.write(f"Product: {product.name}\nStock: {product.stock}\n -----------------------------------------------------\n")
            file.close
    
    # Edit user information
    def LookForProduct(self):
        # Ask the user for input
        product = str(input("Enter the product's name: "))

        # Open the file in read mode
        with open('Inventory.txt', 'r') as file:
            lines = file.readlines()

        # Initialize variables to track user data
        productStart = None
        productEnd = None

        # Find the user's information and record its position
        for i, line in enumerate(lines):
            if line.startswith("Product: " + product):
                productStart = i
                break

        if productStart is not None:
            for i in range(productStart, len(lines)):
                if lines[i].startswith(" -----------------------------------------------------"):
                    productEnd = i
                    break

        # If the user is found, update their age and gender
        if productStart is not None and productEnd is not None:
            print('')
            for i in range(productStart, productEnd + 1):
                print(f"{lines[i]}", end='')
        else:
            print(f"Product '{product}' not found.")

    # Delete user information
    def deleteProduct(self):
        # Ask the user for input
        productToDelete = str(input("Enter the product to delete: "))

        # Open the file in read mode
        with open('Inventory.txt', 'r') as file:
            lines = file.readlines()

        # Initialize variables to track product data
        productStart = None
        productEnd = None

        # Find the user's information and record its position
        for i, line in enumerate(lines):
            if line.startswith("Product: " + productToDelete):
                productStart = i
                break

        if productStart is not None:
            for i in range(productStart, len(lines)):
                if lines[i].startswith(" -----------------------------------------------------"):
                    productEnd = i
                    break

        # If the product is found, delete their information
        if productStart is not None and productEnd is not None:
            del lines[productStart:productEnd + 1]

            # Open the file in write mode and write the updated content
            with open('Inventory.txt', 'w') as file:
                file.writelines(lines)

            print(f"Product '{productToDelete}' deleted successfully.")
        else:
            print(f"Product '{productToDelete}' not found.")
            
    def sortInventory(self):
        try:
            with open("Inventory.txt", 'r') as file:
                lines = file.readlines()

                # Parse the data into a list of dictionaries
                inventory = []
                productInfo = {}
                for line in lines:
                    line = line.strip()
                    if line.startswith("Product: "):
                        productInfo["Product"] = line.replace("Product: ", "")
                    elif line.startswith("Stock: "):
                        productInfo["Stock"] = int(line.replace("Stock: ", ""))
                        inventory.append(productInfo.copy())

            # Sort the inventory by product name
            sortedInventory = sorted(inventory, key=lambda x: x["Product"])

            # Write the sorted inventory back to the file
            with open("Inventory.txt", 'w') as file:
                for item in sortedInventory:
                    file.write(f"Product: {item['Product']}\n")
                    file.write(f"Stock: {item['Stock']}\n")
                    file.write(" -----------------------------------------------------\n")

            return True  # Successfully sorted the inventory
        except FileNotFoundError:
            return False  # File not found


    def main(self):
        while True:
            print("====================================")
            print("            Main Menu")
            print("====================================")
            print(" 0. Exit")
            print(" 1. Add new product")
            print(" 2. Check product")
            print(" 3. Delete product")
            print(" 4. Order Products")
            print("====================================")            
            option = int(input("Enter your option: "))
            match option:
                case 0:
                    self.kill()
                case 1:
                    print("\n")
                    self.AddNewElement()
                case 2:
                    print("\n")
                    self.LookForProduct()
                case 3:
                    print("\n")
                    self.deleteProduct()
                case 4:
                    print("\n")
                    self.sortInventory()
                case _:
                    print("Invalid option")
            print("\n")

init = Main()
init.main()
