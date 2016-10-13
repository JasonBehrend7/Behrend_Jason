username = input("Insert your username here: ")
password = input("Insert your password here: ")

def passCheck(): 
    u = input("To log on, insert your username: ")
    p = input("Now insert your password: ")

    if u == username and p == password:
        print("Access Granted")
    elif u == username or p == password:
        if u == username:
            print("Password is incorrect. Please try again.")
            passCheck()
        else:
            print("Username is incorrect. Please try again.")
            passCheck()
    else:
        print("Username and password are incorrect. Please try again.")
        passCheck()
        
passCheck()
