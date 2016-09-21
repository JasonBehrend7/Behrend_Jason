def reciept(item, price):
    
    print("* \t{:>10} ............. {:10.2f}".format(item, price))
    
item = input("What is your first item: ")
price = float(input("What does it cost: $"))
item2 = input("What is your second item: ")
price2 = float(input("What does it cost: $"))
item3 = input("What is your third item: ")
price3 = float(input("What does it cost: $"))

subtotal = price + price2 + price3
tax = subtotal * .08
total = subtotal + tax

print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
print("""
""")
reciept(item, price)
reciept(item2, price2)
reciept(item3, price3)
print("""
    """)
reciept("Subtotal:", subtotal)
reciept("Tax:", tax)
reciept("Total:", total)
print("_____________________________________________")
print(" * Thank you for your support *")
