def loan(P, r, n, t):

    a = P*(1 + (r/n))**(n*t)
    A = ("{:0.2f}".format(a))
    return A
    
interest = float(input("Type in the interest rate of the loan(%): "))
Principal = float(input("Type in the principal of the loan: "))
compound = float(input("Type in the number of times the loan is compounded per year: "))
life = float(input("Type in the life of the loan(in years): "))
months = life / 12
percent = interest/100

print("The total amount of the loan is $" + str(loan(Principal, percent, compound, months)))


