#!/usr/bin/env python3

from stack_092 import Stack

def matcher(line):
    left = "({["
    right = "]})"
    sq = "[]"
    curly = "{}"
    br = "()"
    s = Stack()

    for c in line:
        try:
            if c in left:
                s.push(c)

            elif c in right and s.top() in sq and c in sq:
                s.pop()

            elif c in right and s.top() in curly and c in curly:
                s.pop()

            elif c in right and s.top() in br and c in br:
                s.pop()
        except:
            return False
    return s.is_empty()
