#!/usr/bin/env python3

import sys

def vowels(words):
    smallest = []
    for w in words:
        if ("a" in w) and ("e" in w) and ("i" in w) and ("o" in w) and ("u" in w):
            smallest.append(w)
    ans = sorted(smallest, key=len)
    return ans[0].strip()

def most_es(words):
    e = 0
    most = []
    for w in words:
        if e < w.lower().count("e"):
            e = w.lower().count("e")
    for word in words:
        if word.strip().lower().count("e") == e:
            most.append(word.strip())
    return most

def main():
    words = []
    for line in sys.stdin:
        words.append(line)
    print("Words containing 17 letters:", [l.strip() for l in words if len(l) == 18])
    print("Words containing 18+ letters:", [l.strip() for l in words if len(l) > 18])
    print("Shortest word containing all vowels:", vowels(words))
    print("Words with 4 a's:", [l.strip() for l in words if l.lower().count("a") == 4])
    print("Words with 2+ q's:", [l.strip() for l in words if l.lower().count("q") >= 2])
    print("Words containing cie:", [l.strip() for l in words if "cie" in l.lower()])
    print("Anagrams of angle:", [l.strip() for l in words if "a" in l.lower() and "n" in l.lower() and "g" in l.lower() and "l" in l.lower() and "e" in l.lower() and len(l) == 6 and "angle" not in l])
    print("Words ending in iary:", len([l.strip() for l in words if l[-5:-1] == "iary"]))
    print("Words with most e's:", most_es(words))

if __name__ == '__main__':
    main()
