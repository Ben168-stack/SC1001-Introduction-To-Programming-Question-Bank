# QUESTION
# ---------
# Given a dictionary where values may repeat, return a list of all keys that
# have a given value.


def abcde(dick, value):
    res = []
    for key in dick:
        if dick[key] == value:
            res.append(key)
    return res


if __name__ == "__main__":
    d = {'a': 2, 'b': 3, 'c': 2, 'd': 5}
    print(abcde(d, 2))
