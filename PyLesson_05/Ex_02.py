item = input("Please enter the first item here: ")
price = float(input("Please enter the price: $"))
item2 = input("Please enter the second item here: ")
price2 = float(input("Please enter the price: $"))
item3 = input("Please enter the third item here: ")
price3 = float(input("Please enter the price: $"))
item4 = input("Please enter the fourth item here: ")
price4 = float(input("Please enter the price: $"))

subtotal = price + price2 + price3 + price4
discount = 0
total = 0

def Discount():
    global subtotal, discount, total
    if subtotal >= 2000:
        discount = .15

    total = subtotal - (subtotal * discount)

def format(item, price):
    print("*{:.<15}........{:.>10.2f}*".format(item, price))

Discount()
print("""

""")
print("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
format(item, price)
format(item2, price2)
format(item3, price3)
format(item4, price4)
format("Subtotal", subtotal)
format("Discount", discount)
format("Total", total)
print("__________________________________")
print("          * THANK YOU *          ") 
