def minimum(list):
    if len(list) == 1:
        return list[0]

    return list[0] if list[0] < minimum(list[1:]) else minimum(list[1:])
