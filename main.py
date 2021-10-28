import user_crud

"""--------Python Examination--------
      IMOGOH ALFRED OHIZUAJEME
"""

db_path = "db/user.json"

def init():
    print("\n**********WELCOME TO HiiT TECH WEBINAR**********\n")
    print("Enter 1 to register for participation")
    print("Enter 2 to exit")

    responses = input("Choose an option\n")

    if responses == "1":
        register()
    elif responses == "2":
        print("Thanks for registering")
    else:
        print("\nInvalid response \nTry again")
        init()

def prompt(message,home_func, retry_func):
    response = input(message)
    if response == "1":
        retry_func()
    else:
        home_func()

def register():
    print("\nProvide the following details to create an account")
    name = input("Enter your full name\n")
    email = input("Enter your email\n")
    mobile_no = input("Enter mobile number: \n")

    
    if name == "" or email == ""or mobile_no =="":
        print("\nThese fields cannot be blank")
    else:
        user_details = {
            "name":name,
            "email":email,
            "mobile_no":mobile_no
        }
        response = user_crud.create_user(db_path,user_details)
        if response == 1:
            print("\nUser creation success")
            print("Redirected home")
            init()
        else:
            print("\nUser with such email account already exist")
            prompt("Enter 1 to retry \nEnter anything to go home", init, register)

init()