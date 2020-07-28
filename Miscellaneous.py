from Useful_Tools import *
from time import sleep


# Shorter way to access the sleep method
def s(seconds):
    sleep(seconds)


def waiting(number_of_dots):
    for dots in range(1, number_of_dots + 1):
        s(1)
        print("." * dots)


def secretQ(number=None):
    if number == 1:
        return "What was a name you gave yourself growing up"
    elif number == 2:
        return "What was your favorite game as a child?"
    elif number == 3:
        return "Where were you when you had your first kiss?"
    elif number == 4:
        return "What is the name of a college you applied to but didn't attend?"
    elif number == 5:
        return "What planet would you like to live on?"
    else:
        print(
            f"\nWhich of these 5 questions would you like to answer? \n{red_bold('Make sure you provide a secure answer you can remember')}"
            "\n\n1. What was a name you gave yourself growing up"
            "\n2. What was your favorite game as a child?"
            "\n3. Where were you when you had your first kiss?"
            "\n4. What is the name of a college you applied to but didn't attend?"
            "\n5. What planet would you like to live on?")
