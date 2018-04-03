
def at(list, x):
    if (x <= 0):
        raise IndexError

    return list[x - 1]

