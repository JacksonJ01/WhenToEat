# Jackson J.
# 12/11/19
# This will tell me when I should eat, how many meals i should eat and the portion size, given that amount
from random import *
Meals = {}
meals1 = []


def rules():
    print("Now remember, you can't merge or split up your meals"
          "\n4 meals means four 1/2 plates, not 2 meals and 2 plates..."
          "\nMathematically yes, but not here")


def number_of_meals():
    input("Press Enter")
    meals = randint(1, 4)
    print("Looks like you'll have " + str(meals) + " for the day")
    happy = input("Are you happy with this number"
                  "\n>>>").title()
    if happy == "Yes" or happy == "Y":
        print("Good")
    elif happy == "No" or happy == "N":
        while happy != "Yes" or happy != "Y":
            meals = randint(1, 4)
            happy = input(f"Your new number is {meals}"
                          f"\nAre happy with this number?"
                          f"\n>>>").title()
            if happy == "Yes" or happy == "Y":
                print(f"Good,", meals, "it is")
                break

    if meals == 1:
        print("You will need to eat a bigger meal for today"
              "\nTwo plates of food doesn't sound like much but you shouldn't over eat")
        meals1.append(1)
    elif meals == 2:
        print("For each meal you should eat one plate of food")
        meals1.append(2)
    elif meals == 3:
        print("2/3 a plate to 3/4 of a plate for your meals")
        meals1.append(3)
    elif meals == 4:
        print("You will need to eat smaller meals today"
              "\n1/2 a plate maximum for each meal")
        meals1.append(4)


def when_to_eat():
    print(meals1[0])
    Meals["Breakfast"] = input("Do you want to eat Breakfast?"
                               "\n>>>").title()
    Meals["Lunch"] = input("What about Lunch?"
                           "\n>>>").title()
    Meals["Dinner"] = input("And is Dinner on the table"
                            "\n>>>").title()
    if Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y"\
            and Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y"\
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")
    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y"\
            and Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y":
        print("")
    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y"\
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")
    elif Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y"\
            and Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")
    elif Meals["Breakfast"] == "Yes" or Meals["Breakfast"] == "Y":
        print("")
    elif Meals["Lunch"] == "Yes" or Meals["Lunch"] == "Y":
        print("")
    elif Meals["Dinner"] == "Yes" or Meals["Dinner"] == "Y":
        print("")


def interface():
    print("\nINTERFACE")
    do = input("What do you want to do?"
               "\n-Rules"
               "\n-Number Of Meals"
               "\n-When To Eat"
               "\n-Exit").title()

    if do == "Rules" or do == "R":
        print("Okay, here are the rules")
        rules()
        interface()
    elif do == "Number Of Meals" or do == "Number" or do == "Of" or do == "Meals" or do == "N" or do == "O" or do == "M":
        number_of_meals()
    elif do == "When To Eat" or do == "When" or do == "To" or do == "Eat" or do == "W" or do == "T" or do == "E":
        when_to_eat()
    elif do == "Exit":
        print("See you later")
        exit()


input("*Click Here Then Press Enter*")

name = input("Hello user, what is your name?"
             "\n>>>").title()
print("Nice to meet you " + name)
decide = input("Are you here because you can't decide on when to eat?"
               "\n>>>").title()
if decide == "Yes" or decide == "Y":
    print("Well you've come to the right place"
          "\nLettuce continue")
elif decide == "No" or decide == "N":
    why = input("So why are you participating in the running of my program?"
                "\n>>>")
    go = input("Ahh, okay then"
               "\nDo you still want to continue with my program?"
               "\n>>>").title()
    if go == "Yes" or go == "Y":
        print("Cool, lettuce continue")
    elif go == "No" or go == "N":
        print("Well someone has their life together"
              "\n🤷")
        exit()
    else:
        while go != "Yes" or go != "Y" or go != "No" or go != "N":
            go = input("Can you repeat that?"
                       "\n>>>").title()
            if go == "Yes" or go == "Y":
                print("Ahh, well you've come to the right place"
                      "\nLettuce continue")
                break
            elif go == "No" or go == "N":
                print("Looks like you're all set and good to go"
                      "\n🤷")
                quit()
else:
    while decide != "Yes" or decide != "Y" or decide != "No" or decide != "N":
        decide = input("Can you repeat that?"
                       "\n>>>").title()
        if decide == "Yes" or decide == "Y":
            print("Lettuce continue then")
            break
        elif decide == "No" or decide == "N":
            why = input("So why are you participating in the running of my program?"
                        "\n>>>")
            go = input("Ahh, okay then"
                       "\nDo you still want to continue with my program?"
                       "\n>>>").title()
            if go == "Yes" or go == "Y":
                print("Cool, lettuce continue")
                break
            elif go == "No" or go == "N":
                print("Well someone has their life together"
                      "\n🤷")
                quit()
            else:
                while go != "Yes" or go != "Y" or go != "No" or go != "N":
                    go = input("Do you want to continue?"
                               "\n>>>").title()
                    if go == "Yes" or go == "Y":
                        print("Lettuce continue then")
                        break
                    elif go == "No" or go == "N":
                        print("Okay, have fun, party pooper")
                        exit()
