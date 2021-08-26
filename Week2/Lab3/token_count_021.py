#!/usr/bin/env python3

import sys

def main():
    tokens = sys.stdin.read()
    tokens = tokens.strip().split()
    print(len(tokens))

if __name__ == '__main__':
    main()
