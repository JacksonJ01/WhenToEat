# To delete a file
import os


def removeFile(filename):
    if os.path.exists(f"{filename}.txt"):
        os.remove(f"{filename}.txt")
    else:
        print(f"The file \"{filename}.txt\" does not exist")

# To remove a folder
# os.rmdir("")


class Fonts:
    purple = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def bold(make_bold):
    return f"{Fonts.bold}{make_bold}{Fonts.end}"


def red_bold(make_bold):
    return f"{Fonts.bold}{Fonts.red}{make_bold}{Fonts.end}"


def under_bold(make_bold):
    return f"{Fonts.bold}{Fonts.underline}{make_bold}{Fonts.end}"


def blue_bold(make_bold):
    return f"{Fonts.bold}{Fonts.blue }{make_bold}{Fonts.end}"
