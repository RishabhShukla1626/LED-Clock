import time
import os 

from datetime import datetime

zero = ["███",
        "█ █",
        "█ █",
        "█ █",
        "███"]

one = ["██ ",
       " █ ",
       " █ ",
       " █ ",
       "███"]

two = ["███",
       "  █",
       "███",
       "█  ",
       "███"]

three = ["███",
         "  █",
         "███",
         "  █",
         "███"]

four = ["█ █",
        "█ █",
        "███",
        "  █",
        "  █"]

five = ["███",
        "█  ",
        "███",
        "  █",
        "███"]

six = ["███",
       "█  ",
       "███",
       "█ █",
       "███"]

seven = ["███",
         "  █",
         "  █",
         "  █",
         "  █"]

eight = ["███",
         "█ █",
         "███",
         "█ █",
         "███"]

nine = ["███",
        "█ █",
        "███",
        "  █",
        "███"]


digits = [zero, one, two, three, four, five, six, seven, eight, nine]

colon = ["   ",
         " █ ",
         "   ",
         " █ ",
         "   "]


while True:


    hour = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second
    clock = [
        digits[hour//10], digits[hour%10],
        colon,
        digits[min//10], digits[min%10],
        colon,
        digits[sec//10], digits[sec%10]
        ]


    for line in range(len(clock[0])):
        for digit in range(len(clock)):
            print(clock[digit][line], end="  ", sep='  ')
        print()
    print()
    time.sleep(1)
    os.system('cls')