# QUESTION
# ---------
# Given two dictionaries, combine them by adding values of matching keys.
#   d1 = {'apple': 3, 'banana': 1}
#   d2 = {'apple': 2, 'carrot': 5}


def mergedict(d1, d2):
    res = {}
    for key, value in d1.items():
        if key not in d2:
            res[key] = value
        elif key in d2:
            res[key] = value + d2[key]
    for key, value in d2.items():
        if key not in res:
            res[key] = value
    return res


if __name__ == "__main__":
    d1 = {'apple': 3, 'banana': 1}
    d2 = {'apple': 2, 'carrot': 5}
    print(mergedict(d1, d2))
