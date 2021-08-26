#!/usr/bin/env python3

def swap_unique_keys_values(d):
    new_d = {}
    for e in d:
        if d[e] not in new_d:
            new_d[d[e]] = e
        else:
            new_d.pop(d[e])
    return new_d
