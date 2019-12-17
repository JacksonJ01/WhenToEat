# Jackson J.
# 12/11/19
# This will tell me when I should eat, how many meals i should eat and the portion size, given that amount

from random import *

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

print("Okay, so in this program, the more meals you have in a day, the smaller the portions")
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
            print("Good")
            break

if meals == 1:
    print("1")
elif meals == 2:
    print("2")
elif meals == 3:
    print("3")
elif meals == 4:
    print("4")
