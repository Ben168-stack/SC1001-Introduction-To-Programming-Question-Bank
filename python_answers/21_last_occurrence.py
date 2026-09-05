# QUESTION
# ---------
# Given a sorted list where numbers may repeat, return the index of the last
# occurrence of the target.


def lastocc(list, target):
    for i in range(len(list)):
        if list[i] == target:
            if list[i + 1] != target:
                return i
    return -1


if __name__ == "__main__":
    test = [1, 2, 2, 2, 3]
    print(lastocc(test, 2))

# NOTE (review): list[i + 1] goes out of range when the target is the last
# element, e.g. lastocc([1, 2, 3], 3) -> IndexError.
