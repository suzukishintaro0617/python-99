
def is_palindrome(list):
    max = len(list)

    for i in range(0, int(max / 2)):
        if (list[i] != list[max - 1 - i]):
            return False

    return True

