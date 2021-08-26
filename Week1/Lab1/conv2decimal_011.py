#!/usr/bin/env python3
 
''' Converts a number in any base (binary = base 2) to decimal '''
import sys
 
def convert(converted):
    digit = converted[0]
    base = converted[1]
    dec = int(digit, int(base))
    return dec
 
def main():
    for line in sys.stdin:
        converted = line.strip().split()
        print(convert(converted))
 
if __name__ == '__main__':
    main()
