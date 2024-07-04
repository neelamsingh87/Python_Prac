# Create a program for entering grocery list which includes code number and price of each item.
# Operations such as adding, deleting and displaying the item should be created.

class Grocery:

    def __init__(self, name, qty, cost):
        self.name = name
        self.qty = qty
        self.cost = cost

    def add_item(self):
        grocery_dict = {
            "name": self.name,
            "quantity": self.qty,
            "cost": self.cost
        }
        return grocery_dict

    def display_item(self):
        print(self.add_item())

    def delete_item(self):
        dict = self.add_item()
        del dict


s1 = Grocery("Maggi", 2, 50)
s2 = Grocery("GoodDay", 10, 10)
s1.add_item()
s2.add_item()
s1.display_item()
s2.display_item()
s1.delete_item()

