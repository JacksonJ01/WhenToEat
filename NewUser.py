from Datebaseconnection import *
from Miscellaneous import *


def newUser():
    input("\nNice to meet you!"
          "\nBefore we get started, you will need to create an account."
          "\nThese are the required pieces of information needed:"
          f"\n- {bold('A Pin Number')}"
          f"\n- {bold('Your First Name')}"
          f"\n- {bold('Your Last Name')}"
          f"\n- {bold('Your Email Address')}"
          f"\n- An {bold('Answer')} to one of the five {bold('Security Questions')} of your choice"
          f"\n\nA pin number is asked before your name to ensure its {bold('uniqueness and privacy')}."
          f"\nThis number can be as long as you'd like it to be, but there is also a {bold('minimum of 4 characters')}."
          f"\n{bold('Press Enter')} when you are ready")

    allSet = False
    pinNumber = input("\nWhat would you like your Pin Number to be?"
                      "\n>>>")
    while allSet is False:
        try:
            pinNumber = int(pinNumber)
            if len(str(pinNumber)) >= 4:  # checks if the length of the pin is at least 4 characters long
                print("\nThe number you entered was at least 4 digits long."
                      "\nLet me check if it is secure enough")
                while True:
                    pin = """
                    SELECT
                      pinNumber
                    FROM
                      userInfo
                    """
                    try:
                        pinNum = read_table(connecting, pin)
                        for pin in pinNum:
                            print(pin)
                            if pinNumber == pin:
                                print("\nLooks like someone has taken that Pin Number."
                                      "\nTry again")
                                int("#Force Fail")
                        print("\nLooks like you're all set")
                        allSet = True
                        break
                    except ValueError:
                        int("#Another Force Fail")
            else:
                print(f"\nYou need to enter a {red_bold('longer')} Pin Number")
                int("#Force Fail")
        except ValueError:
            pinNumber = input(f"\nPlease enter a {red_bold('number')}"
                              "\n>>>")

    firstName = input("\nNow, what is your First Name?"
                      "\n>>>")

    lastName = input("\nAnd your Last Name?"
                     "\n>>>")

    email = input("\nWhat email would you like to link to this program?"
                  "\n>>>")

    secretQ()
    secretQuestion = input(">>>")
    while True:
        try:
            secretQuestion = int(secretQuestion)
            if 0 < secretQuestion < 6:
                break
            else:
                int("#ForceFail")
        except ValueError:
            secretQuestion = input(f"Type a {red_bold('number')} between 1 and 5 to pick a Security Question")

    answer = input("\nWhat is the answer to that question?")

    # This variable contains the string to add this new person using the variables
    add_person = f"""
    INSERT INTO
      userInfo (pinNumber, firstName, lastName, email, secretQuestion, answer)
    VALUES
      ('{pinNumber}', '{firstName}', '{lastName}', '{email}' '{secretQuestion}', '{answer}')"""
    create_table(connecting, add_person)