# QUESTION
# ---------
# Given a list and a target number, implement binary search and return the
# index of the target (or -1 if it isn't there).


def binarysearch(leest, target):
    leest = sorted(leest)
    for i in range(len(leest)):
        if leest[i] == target:
            return i
    return -1


if __name__ == "__main__":
    test1 = [1, 3, 5, 7, 9]
    print(binarysearch(test1, 7))
    print(binarysearch(test1, 6))

# NOTE (review): this is linear search, not binary search - it scans every
# index instead of halving the range. The binary version is the left/right/mid
# loop used in 23_rotated_binary_search.py and 24_mountain_peak.py.
