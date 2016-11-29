math = input("Please enter a mathematical expression: ")
exp = math.split()
i = 0
I = 0
while i < len(exp):
    if exp[i] == "*" or exp[i] == "/":
        if exp[i] == "*":
            exp[i] = float(exp[i-1]) * float(exp[i+1])
            
        else:
            exp[i] = float(exp[i-1]) / float(exp[i+1])
        exp.pop(i-1)
        exp.pop(i)

    i += 1
    
while I < len(exp):
    if exp[I] == "+" or exp[I] == "-":
        if exp[I] == "+":
            exp[I] = float(exp[I-1]) + float(exp[I+1])
            
        else:
            exp[I] = float(exp[I-1]) - float(exp[I+1])
        exp.pop(I-1)
        exp.pop(I)
        
    I += 1
    
print(exp[0])
