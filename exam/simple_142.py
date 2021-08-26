#!/usr/bin/env python3

import sys

# simpl finds the simplicity of each word

def simpl(w):
    count = 0
    tmp = []
    for c in w:
        if c not in tmp:
            count = count + 1
            tmp.append(c)
    return count

def main():
    for line in sys.stdin:
        line = line.strip()
        simplicity = simpl(line)

        if simplicity < 2:
            print(0)
        else:
            print(simplicity - 2)

if __name__ == '__main__':
    main()
