import random
class item:
    def __init__(self, man, name, cat = "", price = ""):
        self.manufacturer = man
        self.name = name
        self.category = cat
        self.UPC = str(random.randint(1000000000, 9999999999))
        self.price = price

    def __str__(self):
        if self.price != "":
            return "\nItem info:\nName: \t \t" + self.name + "\nManufacturer: \t" + self.manufacturer + "\nPrice: \t \t$" + self.price + "\nCategory: \t" + self.category + "\nUPC#: \t \t" + self.UPC
        else:
            return "\nItem info:\nName: \t \t" + self.name + "\nManufacturer: \t" + self.manufacturer + "\nPrice: \t \tNone yet \nCategory: \tNone yet \nUPC#: \t \t" + self.UPC

def main():
    name = input("Enter the name of the item: ")
    man = input("Enter the manufacturer: ")
    question = input("Will you be entering the price and category(Y or N)? ")
    
    if question == "Y":
        price = input("Enter the price of this item: $")
        cat = input("Enter the category of this item: ")
        item1 = item(man, name, cat, price)

    else:
        item1 = item(man, name)

    print(item1.__str__())
main()
