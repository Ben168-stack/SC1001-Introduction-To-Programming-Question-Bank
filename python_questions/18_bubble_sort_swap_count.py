# QUESTION
# ---------
# Modify bubble sort to return how many swaps were performed during sorting.
#
# Then optimise it: stop early once the list is already sorted (i.e. if a full
# pass makes no swaps, break out).


def bubblesortcount(lits):
    pass


def bubblesortopt(lits):
    pass


if __name__ == "__main__":
    print(bubblesortcount([6, 5, 4, 3, 2, 1]))    # expected: ([1..6], 15)
    print(bubblesortopt([1, 2, 3, 4, 5, 6]))      # already sorted -> 0 swaps, 1 pass
