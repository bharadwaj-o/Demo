class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total


# Example usage
cart = ShoppingCart()

cart.add_item("Pepsi", 50)
cart.add_item("Coke", 60)
cart.add_item("Appy", 10)

print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_price = cart.calculate_total()
print("Total Quantity:", total_price)

cart.remove_item("Pepsi")

print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_price = cart.calculate_total()
print("Total Price:", total_price)