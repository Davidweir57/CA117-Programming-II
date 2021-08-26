#!/usr/bin/env python3

def arithmetic(p, q, r=5, s=2):
    return r - p + q + s

def main():

    print(arithmetic(1, 2, 5, 6))

    print(arithmetic(3, 4, 5))

    print(arithmetic(3, 4))

    print(arithmetic(3, 4, s=3))

    print(arithmetic(s=5, q=4, p=2, r=1))

    print(arithmetic(q=2, p=4, 6)) #positional argument follows keyword argument

    print(arithmetic(6, r=2, p=4)) #arithmetic() got multiple values for argument 'p'

    print(arithmetic(p=2, q=4, s=6))

    print(arithmetic(p=5, 2, 5)) #positional argument follows keyword argument


if __name__ == '__main__':
    main()
