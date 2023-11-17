def Welcome():
    print("Welcome to the Text-Based Adventure Game")
    print("PRESS ENTER!!!")
    input()

Welcome()

def Login():
    print("")

while True: 
    print("\nOptions:")
    options = ["1. Login","2. Create New User","EXIT"]

    for option in options:
        print(option)

    select = input("Choose and option:")


Login()




