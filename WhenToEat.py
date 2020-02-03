# Jackson J.
# 12/11/19 - 2/3/2020
# This will tell me when I should eat, how many meals i should eat and the portion size, given that amount
from random import *

Meals = {}
meals1 = []
name1 = []


def user():
    name1.clear()
    name = input("Hello user, what is your name?"
                 "\n>>>").title()
    print("Nice to meet you " + name)
    decide = input("Are you here because you can't decide on when to eat?"
                   "\n>>>").title()

    if decide == "Yes" or decide == "Y":
        print("Well you've come to the right place."
              "\nLettuce continue.")

    elif decide == "No" or decide == "N":
        input("So why are you participating in the running of my program?"
              "\n>>>")
        go = input("Ahh, okay then."
                   "\nDo you still want to continue with my program?"
                   "\n>>>").title()

        if go == "Yes" or go == "Y":
            print("Cool, lettuce continue."
                  "\n*Ahem*")

        elif go == "No" or go == "N":
            print("Well, someone has their life together."
                  "\n🤷")
            exit()

        else:

            while go != "Yes" or go != "Y" or go != "No" or go != "N":
                go = input("Can you repeat that?"
                           "\nDo you want to continue?"
                           "\n>>>").title()

                if go == "Yes" or go == "Y":
                    print("Ahh, well you've come to the right place."
                          "\nLettuce continue.")
                    break

                elif go == "No" or go == "N":
                    print("Looks like you're all set and good to go."
                          "\n🤷")
                    quit()

    else:

        while decide != "Yes" or decide != "Y" or decide != "No" or decide != "N":
            decide = input("Can you repeat that?"
                           "\nCan you not decide when to eat?"
                           "\n>>>").title()

            if decide == "Yes" or decide == "Y":
                print("Lettuce continue then.")
                break

            elif decide == "No" or decide == "N":
                input("So why are you participating in the running of my program?"
                      "\n>>>").title()
                go = input("Ahh, okay then."
                           "\nDo you still want to continue with my program?"
                           "\n>>>").title()

                if go == "Yes" or go == "Y":
                    print("Cool, lettuce continue.")
                    break

                elif go == "No" or go == "N":
                    print("Well someone has their life together."
                          "\n🤷")
                    quit()

                else:

                    while go != "Yes" or go != "Y" or go != "No" or go != "N":
                        go = input("Do you want to continue with my program?"
                                   "\n>>>").title()

                        if go == "Yes" or go == "Y":
                            print("Lettuce continue then.")
                            break

                        elif go == "No" or go == "N":
                            print("Okay, have fun, party pooper.")
                            exit()
                    break
    name1.append(name)
    print("Before I take you to my interface, I advise you to check the rules first.")
    input("Press Enter")
    interface()


def rules():
    print("You can't merge or split up your meals."
          "\n4 meals means four 1/2 plates, not 2 meals and the associated 2 plates..."
          "\nMathematically yes, but not here."
          "\nYou should go to 'Number Of Meals' first"
          "\nYou will be unable to access the When To Eat if you haven't been given meals")
    input("Press Enter")


def number_of_meals():
    meals1.clear()
    meals = randint(1, 3)

    if meals != 1:
        print("Looks like you'll have " + str(meals) + " meals for the day.")

    else:
        print(f"Alright {name1[0]}, you will have {meals} meal today.")

    happy = input("Are you happy with this number."
                  "\n>>>").title()

    if happy == "Yes" or happy == "Y":
        print("Good...")
        meals1.append(meals)

    elif happy == "No" or happy == "N":

        while happy != "Yes" or happy != "Y":
            meals = randint(1, 3)

            if meals != 1:
                happy = input(f"Your new number is {meals} meals."
                              f"\nAre happy with this number?"
                              f"\n>>>").title()

                if happy == "Yes" or happy == "Y":
                    print(f"Good,", meals, " meals it is.")
                    meals1.append(meals)
                    break

                else:
                    print('Let\'s try again then.')

            else:
                happy = input(f"Your new number is {meals} meal."
                              f"\nAre happy with this number?"
                              f"\n>>>").title()

                if happy == "Yes" or happy == "Y":
                    print(f"Good,", meals, " meal it is.")
                    meals1.append(meals)
                    break

                else:
                    print('Let\'s try again then.')

    if meals == 3 and name1[0] == "Jared" or meals == 3 and name1[0] == "J":

        past = input("Woah there."
                     "\nYou thought I wouldn't realize?"
                     "\nYou only have 14 meal passes per week."
                     "\nI'm gonna run this program back."
                     "\nYou can only have a maximum of 2 meals a day, unless of course you've gotten the one meal option this week.."
                     "\n\nDid you eat one meal this past week?"
                     "\n>>>").title()

        if past == "Yes" or past == "Y":
            print("Fine, I guess it's okay for you to have three meals today")

        elif past == "No" or past == "N":
            print("Well then.."
                  "\nLooks like you'll have to get a new number, and you'll have to stick with it.")
            meals = randint(1, 2)
            if meals == 1:
                print("Now you have 1 meal")
                meals1.append(meals)

            elif meals == 2:
                print("Now you have 2 meals")
                meals1.append(meals)


def when_to_eat():
    if meals1[0] != 1 or meals1[0] != 2 or meals1[0] != 3:
        print("You can't come here yet")
        interface()

    Meals.clear()
    print("Okay, ", name1[0], ", you have " + str(meals1[0]) + " meal(s) for today")
    Meals["Breakfast"] = input("Do you want to eat Breakfast?"
                               "\n>>>").title()
    Meals["Lunch"] = input("What about Lunch?"
                           "\n>>>").title()
    Meals["Dinner"] = input("And is Dinner on the table."
                            "\n>>>").title()

    if Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y" \
            and Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y" \
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y" and meals1[0] == 3:
        print("Okay, you have three meals, so you can do this")

    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y" \
            and Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y" \
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y" and meals1[0] != 3:
        print("You don't have three meals!"
              "\n You can't do this")

    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y" \
            and Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y":
        print("")

    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y" \
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")

    elif Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y" \
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")

    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y":
        print("")

    elif Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y":
        print("")

    elif Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")

    interface()


def interface():
    print("\nINTERFACE")
    do = input("What do you want to do? Type the FIRST letter"
               "\n-Rules"
               "\n-Number Of Meals"
               "\n-When To Eat"
               "\n-New User"
               "\n-Exit"
               "\n>>>").title()

    if do == "Rules" or do == "R":
        print("Okay, here are the rules.")
        rules()
        interface()

    elif do == "Number Of Meals" or do == "Number" or do == "Of" or do == "Meals" or do == "N" or do == "O" or do == "M" or do == "Nom":
        number_of_meals()
        interface()

    elif do == "When To Eat" or do == "When" or do == "To" or do == "Eat" or do == "W" or do == "T" or do == "Wte":
        when_to_eat()

    elif do == "New User" or do == "New" or do == "User" or do == "Ne" or do == "U" or do == "Nu":
        print("Ahh, A new user?")
        name1.clear()
        user()

    elif do == "Exit" or do == "E":
        print("See you later.")
        exit()

    elif do != "Rules" or do != "R" \
            or do != "Number Of Meals" or do != "Number" or do != "Of" or do != "Meals" or do != "N" or do != "O" or do != "M" or do != "Nom" \
            or do != "When To Eat" or do != "When" or do != "To" or do != "Eat" or do != "W" or do != "T" or do != "Wte" \
            or do != "New User" or do != "New" or do != "User" or do != "Ne" or do != "U" or do != "Nu" \
            or do != "Exit" or do != "E":
        print("Choose again")
        interface()


input("*Click Here Then Press Enter*")
user()
