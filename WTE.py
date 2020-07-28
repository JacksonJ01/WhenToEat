from Miscellaneous import *
from Datebaseconnection import *


def wte(last_name):
    pinNumber = 0
    firstName = 0
    lastName = 0
    weight = 0
    height = 0
    bmi = 0
    gender = 0
    email = 0
    question = 0
    answer = 0
    goal = 0
    dateTime = 0
    date_time = getDate()

    info = f"""
    SELECT *
    FROM
      userInfo
    WHERE
      lastName = {last_name}
    """
    try:
        info = read_table(connecting, info)
        for information in info:
            pinNumber = information[0]
            firstName = information[1]
            lastName = information[2]
            weight = information[3]
            height = information[4]
            bmi = information[5]
            gender = information[6]
            email = information[7]
            question = information[8]
            answer = information[9]
            goal = information[10]
            dateTime = information[11]
    except TypeError and IndexError:
        print("\nSomething went wrong"
              "\nPlease try again")
    # have a variable for each value
    # do you want to change any of the info before we continue

    do = input("\n1. See your information"
               "\n2. Update Info"
               "\n3. Continue"
               "\n>>>")

    while True:
        try:
            do = int(do)
            if 0 < do < 4:
                break
            else:
                int("#ForceFail")
        except ValueError:
            do = input("\nEnter 1, 2, or 3"
                       "\n>>>")

    sec = secretQ(question)
    if do == 1:
        print(f"\nPin Number: {pinNumber}"
              f"\nFirst Name: {firstName}"
              f"\nLast Name: {lastName}"
              f"\nWeight: {weight}"
              f"\nHeight: {height}"
              f"\nBMI: {bmi}"
              f"\nGender:{gender}"
              f"\nEmail: {email}"
              f"\nSecret Question: {sec}"
              f"\nAnswer: {answer}"
              f"\nGoal: {goal}")
