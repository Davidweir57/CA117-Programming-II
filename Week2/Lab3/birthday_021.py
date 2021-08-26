#!/usr/bin/env python3

import sys
import calendar

def main():
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    dob = calendar.weekday(year, month, day)
    if dob == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    if dob == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    if dob == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    if dob == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    if dob == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    if dob == 5:
        print("You were born on a Saturday and Saturday's child works hard for a living.")
    if dob == 6:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")

if __name__ == '__main__':
    main()
