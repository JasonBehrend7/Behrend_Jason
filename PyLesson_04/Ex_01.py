def reciept(item, price, item2, price2, item3, price3, subtotal, tax, total):
    print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
    print("""

    """)
    print("* \t{:>10} ............. {:10.2f}".format(item, price))
    print("* \t{:>10} ............. {:10.2f}".format(item2, price2))
    print("* \t{:>10} ............. {:10.2f}".format(item3, price3))
    print("""

    """)
    print("* \t{:>10} ............. {:10.2f}".format("Subtotal:", subtotal))
    print("* \t{:>10} ............. {:10.2f}".format("Tax:", tax))
    print("* \t{:>10} ............. {:10.2f}".format("Total:", total))
    print("_____________________________________________")
    print(" * Thank you for your support *")
    
item = input("What is your first item: ")
price = float(input("What does it cost: $"))
item2 = input("What is your second item: ")
price2 = float(input("What does it cost: $"))
item3 = input("What is your third item: ")
price3 = float(input("What does it cost: $"))

subtotal = price + price2 + price3
tax = subtotal * .08
total = subtotal + tax
reciept(item, price, item2, price2, item3, price3, subtotal, tax, total)
