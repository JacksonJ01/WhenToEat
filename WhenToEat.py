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
administratorID = 20019417

print(red_bold(under_bold('\n-To navigate this program type the NUMBER next to the choice you want-')))
input("*Press Enter*")

# This is the main loop for this program
# The menu consist the options that will allow the user to create their account in the the database and access that account
# The admin will be able to view all of the users in the account and remove users if they need to. This can only be accessed with the adminID#
while True:
    menu0 = input("\nHello, are you a New User or and Existing User?"
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

    if menu0 == 1:
        newUser()

    elif menu0 == 2:
        existingUser()

    elif menu0 == 3:
        adminID = input("\nWhat is the Administrator ID?"
                        "\n>>>")

        allUsers = "SELECT * FROM userInfo"
        info = read_table(connecting, allUsers)
        for data in info:
            print(data)

        input("Press enter to delete")
        input(f"Press enter again to {red_bold('delete')}")

        drop_table = """
        DROP TABLE IF EXISTS
          userInfo
        """
        create_table(connecting, drop_table)

        allUsers = "SELECT * FROM userInfo"
        info = read_table(connecting, allUsers)
        for data in info:
            print(data)
