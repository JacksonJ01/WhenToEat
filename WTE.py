from Miscellaneous import *
from Datebaseconnection import *


def wte(pin):
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
    date_time = getM_D_Y_H_M()

    info = f"""
    SELECT *
    FROM
      userInfo
    WHERE
      pinNumber = {pin}
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
    except TypeError:
        print("\nSomething went wrong"
              "\nPlease try again")
    # have a variable for each value
    # do you want to change any of the info before we continue

    if goal == "N/A":
        units = input("\nBefore you continue, I need to ask a couple more questions"
                      "\nFirst off, which unit system do you use?"
                      "\n1. Metric units"
                      "\n2. Imperial units"
                      "\n>>>")
        while True:
            try:
                units = int(units)
                if 0 < units < 3:
                    break
                else:
                    int("#ForceFail")
            except ValueError:
                units = input(red_bold("Enter 1 or 2") +
                              "\n>>>")

        weight = input('\nOkay, now what is your weight?'
                       '\nPeriods can be included, but do not add units'
                       '\n>>>')
        while True:
            try:
                weight = float(weight)
                break
            except ValueError:
                weight = input(red_bold("Do not enter numbers") +
                               "\n>>>")

        height = input('\nAnd what is your height?'
                       '\nPeriods can be included, but do not add units'
                       '\n>>>')
        while True:
            try:
                height = float(height)
                break
            except ValueError:
                height = input(red_bold("Do not enter numbers") +
                               "\n>>>")

        gender = input("What is your gender?"
                       "\n>>>")

        goal = input('\nLast, but not least, what is your goal?'
                     '\n1. Lose weight and get Leaner'
                     '\n2. Maintain current weight'
                     '\n3. Gain weight and Bulk up'
                     '\n>>>')
        while True:
            try:
                goal = int(goal)
                if goal == 1:
                    goal = "Get Leaner"
                elif goal == 2:
                    goal = "Maintain Weight"
                elif goal == 3:
                    goal = "Bulk up"
                else:
                    int("#Force Fail")
                break
            except ValueError:
                goal = input(red_bold("Enter 1, 2, or 3") +
                             "\n>>>")

        if units == 1:
            bmi = float(weight / (height**2))
        elif units == 2:
            bmi = float(weight / (height**2) * 703)

        info = f"""
        UPDATE
          userInfo
        SET
          height = {height},
          weight = {weight},
          bmi = {bmi},
          gender = {gender},
          goal = {goal}
        WHERE
          pinNumber = {pinNumber}
        """
        try:
            create_table(connecting, info)
        except Error:
            print("There was a problem while trying to add your information to the database"
                  "Contact the Admin")
            return

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
    journal = False
    if do == 1:
        print(f"\nPin Number: {pinNumber}"
              f"\nFirst Name: {firstName}"
              f"\nLast Name: {lastName}"
              f"\nWeight: {weight}"
              f"\nHeight: {height}"
              f"\nBMI: {bmi}"
              f"\nGender:{gender}"
              f"\nEmail: {email}"
              f"\nSecurity Question: {sec}"
              f"\nAnswer: {answer}"
              f"\nGoal: {goal}"
              f"\nLast Login: {dateTime}")
        input("Press Enter")

        return wte(lastName)

    if do == 2:
        updateInfo = input("\nWhat would you like to update?"
                           "\n1. Name"
                           "\n2. Weight and Height"
                           "\n3. Goal"
                           "\n4. Gender"
                           "\n>>>")
        while True:
            try:
                updateInfo = int(updateInfo)
                if 0 < updateInfo < 5:
                    break
                else:
                    int("#ForceFail")

            except ValueError:
                updateInfo = input(red_bold("\nTry Again\nPlease enter 1, 2, 3, or 4") +
                                   "\n>>>")

        ###########################
        if updateInfo == 1:
            fName = input("\nWhat is your First Name"
                          '\n>>>')
            lName = input("\nWhat is your Last Name"
                          "\n>>>")

            updateName = """
            """

        elif updateInfo == 2:
            units = input("\nWhich unit system would you like to use?"
                          "\n1. Metric units"
                          "\n2. Imperial units"
                          "\n>>>")
            while True:
                try:
                    units = int(units)
                    if 0 < units < 3:
                        break
                    else:
                        int("#ForceFail")
                except ValueError:
                    units = input(red_bold("Enter 1 or 2") +
                                  "\n>>>")

            weight = input('\nWhat is your weight?'
                           '\nPeriods can be included, but do not add units'
                           '\n>>>')
            while True:
                try:
                    weight = float(weight)
                    break
                except ValueError:
                    weight = input(red_bold("Do not enter numbers") +
                                   "\n>>>")

            height = input('\nAnd your height?'
                           '\nPeriods can be included, but do not add units'
                           '\n>>>')
            while True:
                try:
                    height = float(height)
                    break
                except ValueError:
                    height = input(red_bold("Do not enter numbers") +
                                   "\n>>>")

            if units == 1:
                bmi = float(weight / (height**2))
            elif units == 2:
                bmi = float(weight / (height**2) * 703)

        elif updateInfo == 3:
            goal = input('\nLast, but not least, what is your goal?'
                         '\n1. Lose weight and get Leaner'
                         '\n2. Maintain current weight'
                         '\n3. Gain weight and Bulk up'
                         '\n>>>')
            while True:
                try:
                    goal = int(goal)
                    if goal == 1:
                        goal = "Get Leaner"
                    elif goal == 2:
                        goal = "Maintain Weight"
                    elif goal == 3:
                        goal = "Bulk up"
                    else:
                        int("#Force Fail")
                    break
                except ValueError:
                    goal = input(red_bold("Enter 1, 2, or 3") +
                                 "\n>>>")
        elif updateInfo == 4:
            gender = input("\nWhat is your gender")

        return wte(pin)

    if do == 3:
        if "00:00" < date_time[12:] < "07:00":
            miss = input("\nYou've arrived during the down time period"
                         "\nDid you miss the Check-In period? (Y or N)"
                         "\n>>>")
            if miss == 'Y':
                journal = True
            else:
                "\nOkay, come back at 7 am"

        if "21:00" < date_time[12:] <= "00:00" or journal is True:
            print("\nLet me check your file")
            waiting(3)

        rand = r(1, 30)
        if "07:00" <= date_time[12:] <= "11:00":
            if goal == "Lean":
                if rand < 16:
                    print(f"\nSkip breakfast for today")
                else:
                    print("\nEach 1 plate of food")

            if goal == "Maintain":
                print(f"\n")

            if goal == "Bulk":
                print(f"\n")

        elif "11:00" < date_time[12:] <= "15:00":
            if goal == "Lean":
                print(f"\nIf you skipped breakfast today you should eat 1 plate of food for lunch")

            if goal == "Maintain":
                print(f"\n")

            if goal == "Bulk":
                print(f"\n")

        elif "15:00" < date_time[12:] <= "21:00":
            if goal == "Lean":
                print(f"\nYou should eat 1 heaping plate of food")

            if goal == "Maintain":
                print(f"\n")

            if goal == "Bulk":
                print(f"\n")

        update = f"""
        UPDATE TABLE
          userInfo
        SET
          dateTime = {date_time}
        WHERE
          pinNumber = {pinNumber}
        """
        try:
            create_table(connecting, update)
        except Error:
            print("Something went wrong")

        return wte(lastName)
