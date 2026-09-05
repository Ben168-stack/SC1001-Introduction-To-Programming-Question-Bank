# QUESTION
# ---------
# Given a sorted list where numbers may repeat, return the index of the last
# occurrence of the target. Return -1 if it isn't there.


def lastocc(list, target):
    pass


if __name__ == "__main__":
    print(lastocc([1, 2, 2, 2, 3], 2))     # expected: 3
    print(lastocc([1, 2, 3], 3))           # expected: 2 (target is last element)
    print(lastocc([1, 2, 3], 9))           # expected: -1
