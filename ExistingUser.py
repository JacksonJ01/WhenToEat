from Datebaseconnection import *
from Miscellaneous import *


def existingUser():
    print(f"\n{red_bold('Press 0')} if you forgot your Pin Number"
          f"\n{red_bold('Press 1')} if you do not have an account")
    pin = input(f"\nEnter your {bold('Pin Number')}"
                f"\n>>>")
    while True:
        try:
            pin = int(pin)
            if pin == 0:
                first_Name = input("Okay, what is your first name?")
                last_Name = input("What is your last name")
            elif pin == 1:
                print()
            elif len(str(pin)) >= 4:
                first_Name = input("Okay, what is your first name?")
                last_Name = input("What is your last name")
                pinNum = """"""
            else:
                int("#ForceFail")
        except ValueError:
            pin = input(f"Please enter {red_bold('0, 1, or your PIN NUMBER')}")
