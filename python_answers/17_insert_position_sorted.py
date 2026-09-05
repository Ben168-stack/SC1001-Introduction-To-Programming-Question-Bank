# QUESTION
# ---------
# Given a sorted list and a target, return the index where the target should be
# inserted to keep the list sorted.


def insertarg(lis, target):
    for i in range(len(lis)):
        if lis[i] >= target:
            lis.insert(i, target)
            return lis
    lis.append(target)
    return lis


if __name__ == "__main__":
    lis = [5, 10, 20]
    print(insertarg(lis, 3))

# NOTE (review): the question asks for the index, but this returns the whole
# list with the target inserted (and mutates the input list).
