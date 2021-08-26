#!/usr/bin/env python3

import sys

def name(email):
    i = 0
    while email[1][i] < "0" or "9" < email[1][i]:
        i = i + 1
    return email[0].capitalize() + " " + email[1][:i].capitalize()

def main():
    for line in sys.stdin:
        email = line.strip().split(".")
        print(name(email))

if __name__ == '__main__':
    main()
