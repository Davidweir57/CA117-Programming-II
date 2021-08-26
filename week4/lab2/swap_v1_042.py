#!/usr/bin/env python3

def swap_keys_values(d):
    new_d = {}
    for e in d:
        new_d[d[e]] = e
    return new_d
