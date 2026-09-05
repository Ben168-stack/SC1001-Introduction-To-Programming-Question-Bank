# QUESTION
# ---------
# Given a sorted list and a target number, implement binary search and return
# the index of the target (or -1 if it isn't there).
#
# Binary search means halving the search range each step (left / mid / right),
# NOT scanning every index.


def binarysearch(leest, target):
    pass


if __name__ == "__main__":
    test1 = [1, 3, 5, 7, 9]
    print(binarysearch(test1, 7))    # expected: 3
    print(binarysearch(test1, 6))    # expected: -1
