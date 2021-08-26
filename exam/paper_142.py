#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.split()
        p1 = line[0]
        p2 = line[1]

        if p1 == p2:
            print("Draw")
        elif p1 == "paper" and p2 == "rock":
            print("Player 1 wins")
        elif p1 == "rock" and p2 == "scissors":
            print("Player 1 wins")
        elif p1 == "scissors" and p2 == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

if __name__ == '__main__':
    main()
