from Datebaseconnection import *
from Miscellaneous import *


def newUser():
    print("\nNice to meet you!"
          "\nBefore we get started, you will need to create an account."
          "\nThese are the required pieces of information needed:"
          f"\n- {bold('A Pin Number')}"
          f"\n- {bold('Your First Name')}"
          f"\n- {bold('Your Last Name')}"
          f"\n- {bold('Your Email Address')}"
          f"\n- An {bold('Answer')} to one of the five {bold('Security Questions')} of your choice")
    s(2)
    input(f"\n\nA pin number is asked before your name to ensure its {bold('uniqueness and privacy')}."
          f"\nThis number can be as long as you'd like it to be, but there is also a {bold('minimum of 4 characters')}."
          f"\nShould you forget this pin number, the email you provide will serve as a means to help retrieve your pin"
          f"\nIf you do not remember the pin number nor the email you linked you can request the Administrator's help"
          f"\n\n{bold('Press Enter')} when you are ready")

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
                            if pinNumber == pin[0]:
                                waiting(2)
                                print("\nLooks like someone has taken that Pin Number."
                                      "\nTry again")
                                int("#Force Fail")
                        waiting(3)
                        print("\nLooks like you're all set")
                        allSet = True
                        break
                    except ValueError and TypeError:
                        int("#Another Force Fail")
            else:
                print(f"\nYou need to enter a {red_bold('longer')} Pin Number")
                int("#Force Fail")
        except ValueError:
            pinNumber = input(f"\nPlease enter a {red_bold('number')}"
                              "\n>>>")

    firstName = input("\nNow, what is your First Name?"
                      "\n>>>").title().strip()

    lastName = input("\nAnd your Last Name?"
                     "\n>>>").title().strip()

    email = input("\nWhat email would you like to link to this program?"
                  "\n>>>").lower().strip()
    while True:
        check = """
        SELECT
          email
        FROM
          userInfo
        """
        try:
            checking = read_table(connecting, check)
            for check in checking:
                if check[0] == email:
                    print("That email address is taken")
                    int("#ForceFail")
            print("The email you provided is available")
            break
        except TypeError:
            print("The email you provided is available")
        except ValueError:
            email = input("\nTry again"
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
            secretQuestion = input(f"Type a {red_bold('number')} between 1 and 5 to pick a Security Question"
                                   f"\n>>>")

    answer = input("\nWhat is the answer to that question?"
                   "\n>>>").lower()

    dateTime = getM_D_Y_H_M()

    # This variable contains the string to add this new person using the variables
    add_person = f"""
    INSERT INTO
      userInfo (pinNumber, firstName, lastName, gender, weight, height, bmi, email, secretQuestion, answer, goal, dateTime)
    VALUES
      ('{pinNumber}', '{firstName}', '{lastName}', 'N/A', 'N/A', 'N/A', 'N/A', '{email}', '{secretQuestion}', '{answer}', 'N/A', '{dateTime}')"""
    create_table(connecting, add_person)

    createFile = f"""
    INSERT INTO
      userFileName (pinNumber)
    VALUES
      ('{pinNumber}')"""
    create_table(connecting, createFile)

    getFileName = f"""
    SELECT
      fileName
    FROM
      userFileName
    WHERE
      pinNumber = {pinNumber}
    """
    sec = secretQ(secretQuestion)
    try:
        file = read_table(connecting, getFileName)
        for fileName in file:
            file = fileName[0]
        create = open(f"{file}.txt", "w")
        create.write(f"""PIN NUMBER: {pinNumber}
FIRST NAME: {firstName}
LAST NAME: {lastName}
GENDER: N/A
WEIGHT: N/A
HEIGHT: N/A
BMI: N/A
EMAIL: {email}
SECRET QUESTION: {sec}
ANSWER: {answer}
GOAL: N/A
DATE TIME: {dateTime}
\n""")
        create.close()
    except TypeError and IndexError:
        print("\nSomething went wrong"
              "\nPlease Contact The Admin")

    return pinNumber
