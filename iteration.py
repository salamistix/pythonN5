password = input("what is your password? ")
passwordcheck = input("re-enter your password? ")

valid = False
while valid == False:
    print("what is your password? ")
    enterpassword = input()
    if enterpassword != password:
        print("invalid password ")
        print("what is your password? ")
        enterpassword = input()
    else: 
        valid = True
        print("correct password")