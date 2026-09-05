# QUESTION
# ---------
# Input: a dictionary like
#   {"Apple": 5, "Banana": 8, "Carrot": 10, "Berry": 4}
# Return the sum of values whose keys start with 'A' or 'B'.


def istilldk(dick):
    sum = 0
    for key in dick:
        kay = key.lower()
        if kay[0] == 'a' or kay[0] == 'b':
            sum += dick.get(key)
    return sum


if __name__ == "__main__":
    deeck = {"Apple": 5, "Banana": 8, "Carrot": 10, "Berry": 4}
    print(istilldk(deeck))
