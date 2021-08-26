def reverse_list(l):
    if len(l) < 2:
        return l
    return [l[-1]] + reverse_list(l[:-1])
