while True:
    email= str(input("Please enter your e mail"))
    if not("." in email) or not("@" in email):
        print("You cant use that it is not valid")
    else:
        print("It is valid")
        break