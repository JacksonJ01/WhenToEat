from Datebaseconnection import *
from Miscellaneous import *


def existingUser():
    print(f"\n{red_bold('Press 0')} if you forgot your Pin Number"
          f"\n{red_bold('Press 1')} if you do not have an account"
          f"\n{red_bold('Press 2')} to leave this screen")
    pin = input(f"\nEnter your {bold('Pin Number')}"
                f"\n>>>")
    while True:
        try:
            pin = int(pin)
            if pin == 0:
                done = False
                while done is False:
                    first_Name = input("\nWhat is your first name?"
                                       "\n>>>").title()
                    last_Name = input("\nWhat is your last name"
                                      "\n>>>").title()
                    email = input("\nWhat is the the email linked to your account?"
                                  "\n>>>").lower()

                    forgot = f"""
                    SELECT
                      pinNumber, secretQuestion, answer
                    FROM
                      userInfo
                    WHERE
                      firstName = '{first_Name}' and lastName = '{last_Name}' and email = '{email}'
                    """

                    try:
                        forgotten = read_table(connecting, forgot)
                        existingPin = 0
                        sQ = 0
                        ans = 0
                        for recover in forgotten:
                            existingPin = recover[0]
                            sQ = recover[1]
                            ans = recover[2]

                        if existingPin == 0:
                            print("\nThe information you entered did not match our records"
                                  "\nPlease try again")
                            existingUser()

                        print(secretQ(sQ))
                        answer = input(">>>")
                        if answer == ans:
                            change = input(f"\nYour Pin Number is {red_bold(existingPin)}"
                                           f"\nWould you like to change it?"
                                           f"\nY or N"
                                           f"\n>>>").title()
                            if change == 'Y':
                                successful = False
                                while not successful:
                                    change = input("\nWhat would you like to change your Pin Number to?"
                                                   "\n>>>")
                                    while True:
                                        try:
                                            change = int(change)
                                            if len(str(change)) >= 4:
                                                break
                                            else:
                                                int("#Force Fail")
                                        except ValueError:
                                            change = input(f"\nPlease enter new Pin Number with a {bold('minimum of 4 digits')}"
                                                           f"\n>>>")

                                    checkPin = """
                                    SELECT
                                      pinNumber
                                    FROM
                                      userInfo"""
                                    try:
                                        checking = read_table(connecting, checkPin)
                                        for check in checking:
                                            if check[0] == change:
                                                print("\nThat Pin Number is taken, try again")
                                                int('#Force Fail')
                                        newPinNumber = f"""
                                        UPDATE
                                          userInfo
                                        SET
                                          pinNumber = {change}
                                        WHERE
                                          pinNumber = {existingPin}"""
                                        try:
                                            create_table(connecting, newPinNumber)
                                            successful = True
                                            done = True
                                        except Error:
                                            print("Something went wrong, try again")

                                    except Error and ValueError:
                                        print("")
                            else:
                                existingUser()
                    except Error:
                        print("\nThe information you provided does not match any record in the database"
                              "\nPlease try again")

            elif pin == 1:
                return 1

            elif pin == 2:
                return 0

            elif len(str(pin)) >= 4:
                first_Name = input("\nOkay, what is your first name?"
                                   "\n>>>").title()
                last_Name = input("\nWhat is your last name"
                                  "\n>>>").title()
                pinNumCheck = f"""
                SELECT 
                  firstName, lastName
                FROM
                  userInfo  
                WHERE
                  pinNumber = {pin}             
                """
                try:
                    check = read_table(connecting, pinNumCheck)
                    for checking in check:
                        if checking[0] == first_Name and checking[1] == last_Name:
                            print("Welcome Back", first_Name)
                            return last_Name
                    print("\nThe information you entered did not match with our records."
                          "\nPlease try again")
                except Error:
                    print("\nSomething went wrong..."
                          "\nPlease try again")
                finally:
                    existingUser()
            else:
                int("#ForceFail")
        except ValueError:
            pin = input(f"Please enter {red_bold('0, 1, or your PIN NUMBER')}")
