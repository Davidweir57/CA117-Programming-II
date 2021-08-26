#!/usr/bin/env python3

import sys

def main():
    hand = []
    for line in sys.stdin:
        line = line.strip()
        hand.append(line[-1])

    print("The probability of nothing is {:.4f}%".format(((hand.count("0") / len(hand)) * 100)))
    print("The probability of one pair is {:.4f}%".format((hand.count("1")) / len(hand) * 100))
    print("The probability of two pairs is {:.4f}%".format((hand.count("2")) / len(hand) * 100))
    print("The probability of three of a kind is {:.4f}%".format((hand.count("3")) / len(hand) * 100))
    print("The probability of a straight is {:.4f}%".format((hand.count("4")) / len(hand) * 100))
    print("The probability of a flush is {:.4f}%".format((hand.count("5")) / len(hand) * 100))
    print("The probability of a full house is {:.4f}%".format((hand.count("6")) / len(hand) * 100))
    print("The probability of four of a kind is {:.4f}%".format((hand.count("7")) / len(hand) * 100))
    print("The probability of a straight flush is {:.4f}%".format((hand.count("8")) / len(hand) * 100))
    print("The probability of a royal flush is {:.4f}%".format((hand.count("9")) / len(hand) * 100))

if __name__ == '__main__':
    main()
