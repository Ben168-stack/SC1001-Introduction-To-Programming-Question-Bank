# QUESTION
# ---------
# Merge Sort - Count Inversions
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
# Modify merge sort to count how many inversions are in the list.
#   Example: [3, 1, 2] -> 2 inversions (3 > 1, 3 > 2)
#
# Careful: the total is the inversions found in the left half, plus those in
# the right half, plus those found while merging the two.


def merge2(left, right):
    pass


def mergesort2(list):
    pass


if __name__ == "__main__":
    print(mergesort2([3, 1, 2]))                  # expected: ([1, 2, 3], 2)
    print(mergesort2([5, 4, 3, 2, 1]))            # expected: ([1..5], 10)
