#!/usr/bin/env python3

import sys

def main():
    try:
        file = sys.argv[1]
        with open(file, "r") as f:
            biggest = 0
            names = ""
            for line in f:
                details = line.strip().split()
                try:
                    marks = line.strip()
                    if int(marks[0:2]) == biggest:
                        names = names + ", " + marks[3:]
                    elif int(marks[0:2]) > biggest:
                        biggest = int(marks[0:2])
                        names = marks[3:]
                except(ValueError):
                    print("Invalid mark" + " " + str(marks[0:2]) + " " + "encountered. Skipping.")
            print("Best student(s):" + " " + names)
            print("Best mark:" + " " + str(biggest))
    except(FileNotFoundError):
        print("Error")

if __name__ == '__main__':
    main()
