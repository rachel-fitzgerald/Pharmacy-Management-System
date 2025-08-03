# -------------------------------
# Pharmacy Management System
# -------------------------------

# Class to store medicine info
class Medicine:
    def __init__(self, name, quantity, price, expiry):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.expiry = expiry

# Inventory will store all medicines
class Inventory:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, name, quantity, price, expiry):
        # Check if the medicine already exists
        for med in self.medicines:
            if med.name == name:
                med.quantity += quantity
                print(f"Updated {name}: {med.quantity} in stock")
                return
        # If it doesn't exist, add new
        new_med = Medicine(name, quantity, price, expiry)
        self.medicines.append(new_med)
        print(f"Added new medicine: {name}")

    def show_inventory(self):
        if not self.medicines:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for med in self.medicines:
                print(f"{med.name} - {med.quantity} units - ${med.price} - Exp: {med.expiry}")

    def sell_medicine(self, name, sell_qty):
        for med in self.medicines:
            if med.name == name:
                if sell_qty <= med.quantity:
                    total = sell_qty * med.price
                    med.quantity -= sell_qty
                    print(f"Sold {sell_qty} units of {name}")
                    print(f"Total Bill: ${total:.2f}")
                    return
                else:
                    print(f"Not enough stock for {name}")
                    return
        print(f"Medicine {name} not found.")

# Main function for interaction
def main():
    inventory = Inventory()

    while True:
        print("\n--- Pharmacy Menu ---")
        print("1. Add Medicine")
        print("2. Show Inventory")
        print("3. Sell Medicine")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Medicine name: ")
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price per unit: "))
                expiry = input("Expiry date (YYYY-MM-DD): ")
                if quantity <= 0 or price <= 0:
                    print("Quantity and price must be positive.")
                    continue
                inventory.add_medicine(name, quantity, price, expiry)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "2":
            inventory.show_inventory()
        elif choice == "3":
            name = input("Medicine to sell: ")
            try:
                qty = int(input("Quantity to sell: "))
                inventory.sell_medicine(name, qty)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
