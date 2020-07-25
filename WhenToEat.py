# Jackson J.
# 12/11/19 - 2/3/2020
# This will tell me, or other users when I should eat, how many meals i should eat and the portion size, given that amount
#
# Ask user some questions in menu format and save the number in a variable:
# - Name(not formatted)
# - Time of day
# - when they last ate
# - meal or snack
# - how hungry they are
# - if exercised today
# - if no then will
#
# Ask what the users intentions are:
# - Lean
# - Bulk
# - Maintain
#
# "\n1. 12am - 3am" +   ////
# "\n2. 3am  - 6am" +   //
# "\n3. 6am  - 9am" +   //
# "\n4. 9am  - 12pm" +  ///
# "\n5. 12pm - 3pm" +   ///
# "\n6. 3pm  - 6pm" +   ///
#  "\n7. 6pm  - 9pm" +   ////
#  "\n8. 9pm  - 12am");  ////
from NewUser import *
from ExistingUser import *

when = 0
plates = 0
calories = 0
administratorID = 20019417  # By default this code will be 0000, but it should be changed for security

print(red_bold(under_bold('\n-To navigate this program type the NUMBER next to the choice you want-')))
input("*Press Enter*")

# This is the main loop for this program
# The menu consist the options that will allow the user to create their account in the the database and access that account
# The admin will be able to view all of the users in the account and remove users if they need to. This can only be accessed with the adminID#
while True:
    menu0 = input("\nHello, are you a New User or an Existing User?"
                  "\n1. New User"
                  "\n2. Existing User"
                  "\n3. Administrator"
                  "\n4. Exit Program"
                  "\n>>>")
    while True:
        try:
            menu0 = int(menu0)
            if 0 < menu0 < 5:
                break
            else:
                int("#ForceFail")
        except ValueError:
            menu0 = input(f"\n{red_bold('Press 1')} if you are a New User"
                          f"\n{red_bold('Press 2')} if you are an Existing User"
                          f"\n{red_bold('Press 3')} if you are an Admin"
                          f"\n{red_bold('Press 4')} if you want to Leave"
                          f"\n>>>")

    user = 0
    if menu0 == 1:
        user = newUser()

    elif menu0 == 2:
        user = existingUser()
        if user == 1:
            newUser()

    elif menu0 == 3:
        isAdmin = input("\nWhat is the Administrator ID?"
                        "\n>>>")
        while True:
            try:
                isAdmin = int(isAdmin)
                if isAdmin == administratorID:
                    while True:
                        overseer = input(f"\nADMIN MENU"
                                         f"\n0. {bold('See All User Info')}"
                                         f"\n1. {red_bold('DELETE')} {bold('A User')}"
                                         f"\n2. {red_bold('DELETE ALL USERS')}"
                                         f"\n3. {bold('Exit Menu')}"
                                         f"\n>>>")
                        while True:
                            try:
                                overseer = int(overseer)
                                if 0 <= overseer < 4:
                                    break
                                else:
                                    int("#ForceFail")
                            except ValueError:
                                overseer = input(f"\n{red_bold('Press 0')} to see USER INFO"
                                                 f"\n{red_bold('Press 1')} to {bold(red_bold('DELETE') + ' A User')}"
                                                 f"\n{red_bold('Press 2')} to {red_bold('DELETE ALL USERS')}"
                                                 f"\n{red_bold('Press 3')} to Exit this menu"
                                                 f"\n>>>")

                        if overseer == 0:
                            allUsers = "SELECT * FROM userInfo"
                            info = read_table(connecting, allUsers)
                            for data in info:
                                print(f"\nPin Number: {data[0]} | First Name: {data[1]} |Last Name: {data[2]} | Gender: {data[3]} | Weight: {data[4]} | Height: {data[5]} " 
                                      f"\nBMI: {data[6]} | Email: {data[7]} | Security Question: {data[8]} | Answer: {data[9]} | Goal: {data[10]} | Previous Day: {data[11]}")

                        elif overseer == 1:
                            delete = input(f"\nWhat is the {red_bold('PIN NUMBER')} of the account you wish to delete"
                                           f"\n>>>")
                            dropAccount = f"""
                            DELETE FROM
                              userInfo
                            WHERE
                              pinNumber = {delete}
                            """
                            try:
                                deleting = create_table(connecting, dropAccount)
                            except Error as welp:
                                print(welp)

                        elif overseer == 2:
                            drop_table = """
                            DROP TABLE IF EXISTS
                              userInfo"""
                            create_table(connecting, drop_table)

                        elif overseer == 3:
                            break
                    break
                else:
                    int("#ForceFail")
            except ValueError:
                isAdmin = input(f"\n{red_bold('Incorrect PIN NUMBER')}"
                                "\nTry Again"
                                "\n>>>")

    elif menu0 == 4:
        print("Have A Good Day")
        exit()

    if user != 0:
        print("")
