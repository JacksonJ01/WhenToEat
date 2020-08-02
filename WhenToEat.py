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
#  -Instead of me asking the user what time of day it is, i can access the time through the computer
#   - If it falls into the category...
#    - 9pm - 12 am is the check in period
#    - 12 am 7 am is the gray area
#    - 7 am - 11 am is breakfast period
#    - 11 am - 3 pm is the lunch period
#    - 3pm to 9 pm is the dinner period
#
#    update the previousday to hold the current date whenever the user logs in
#    change the 0 to forgot or want to change#
#
# - menu for existing users that will allow them to change the information they provided as a new user#
#
# I might add an auto increment to the userInfo table because it will help me keep track of the users files better
# - I can't make the file name the users name because names are not unique
# - I can make the user Pin Number the file name, but the pin can be changed,
#  -so i would have create a new file with the new pin name, copy the info, and delete the old file
# - Instead I will create a file column in the table and have it auto increment (I can also make that number a primary key),
# - then use that number for the file name, but i will probably add "User" in front of it
# - The admin can remove users from the database, so i will have to also remove the file linked to them
#  - I can use regular expressions to parse the file that will hold the Existing User file names and I can modify that file to delete
#  - If I have a temporary variable in the loop that reads the file, I can add the names to it, but when it reaches the file
#   - "User#" I can skip it and I can use the os module to delete the path to the file#
#  - I could also create a database specifically for the file names and have then linked...
# - The admin can delete the whole database, so i will also have to delete every file that exists for the users
#  - I can delete the files that exist as I loop through the "userFileName" database
#  - Then I can delete the whole database#
from ExistingUser import *
from WTE import *

when = 0
plates = 0
calories = 0
administratorID = 20011002  # By default this code will be 20011002, but it should be changed for security

print(red_bold(under_bold('-To navigate this program type the NUMBER next to the choice you want-')))
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
                          f"\n{red_bold('Press 4')} if you want to Exit"
                          f"\n>>>")

    if menu0 == 1:
        wte(newUser())

    elif menu0 == 2:
        wte(existingUser())

    elif menu0 == 3:
        attempts = 3
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
                            try:
                                allUsers = "SELECT * FROM userInfo"
                                info = read_table(connecting, allUsers)
                                if info[0] is None:
                                    int("#Force Fail")
                                for data in info:
                                    print(f"\nPin Number: {data[0]} | First Name: {data[1]} |Last Name: {data[2]} | Gender: {data[3]} | Weight: {data[4]} | Height: {data[5]} " 
                                          f"\nBMI: {data[6]} | Email: {data[7]} | Security Question: {data[8]} | Answer: {data[9]} | Goal: {data[10]} | Last Login: {data[11]}")
                            except ValueError and IndexError:
                                print("\nThe database is currently empty")

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
                                create_table(connecting, dropAccount)
                            except Error:
                                print("The database does not have a User linked the that Pin Number")
                            try:
                                deleteFile = f"""
                                SELECT
                                  fileName
                                FROM
                                  userFileName
                                WHERE
                                  pinNumber = {delete}"""
                                file = read_table(connecting, deleteFile)
                                for files in file:
                                    file = files[0]
                                removeFile(f"{file}")
                            except Error as welp:
                                print(welp)

                            deleteUserFile = f"""
                            DELETE FROM
                              userFileName
                            WHERE
                              pinNumber = {delete}
                            """
                            try:
                                create_table(connecting, deleteUserFile)
                            except Error:
                                print("")

                        elif overseer == 2:
                            drop_table = """
                            DROP TABLE IF EXISTS
                              userInfo"""
                            create_table(connecting, drop_table)

                            getFileName = """
                            SELECT 
                              fileName
                            FROM
                              userFileName
                            """
                            try:
                                file = read_table(connecting, getFileName)
                                for currentFile in file:
                                    removeFile(f"{currentFile[0]}")
                            except TypeError and IndexError:
                                print("\nThere are no File Names in this database")

                            drop_again = """
                            DROP TABLE IF EXISTS
                              userFileName"""
                            create_table(connecting, drop_again)

                            create_table(connecting, personTable)
                            create_table(connecting, userFileTable)

                        elif overseer == 3:
                            break
                    break
                else:
                    int("#ForceFail")
            except ValueError:
                attempts -= 1
                if attempts == 0:
                    break
                isAdmin = input(f"\n{red_bold('Incorrect PIN NUMBER')}"
                                f"\n{red_bold(f'{attempts} attempt(s) left')}"
                                "\nTry Again"
                                "\n>>>")

    elif menu0 == 4:
        print("Have A Good Day")
        exit()
