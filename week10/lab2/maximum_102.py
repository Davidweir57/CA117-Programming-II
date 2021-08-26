def maximum(list):
    if len(list) == 1:
        return list[0]

    return list[0] if list[0] > maximum(list[1:]) else maximum(list[1:])
