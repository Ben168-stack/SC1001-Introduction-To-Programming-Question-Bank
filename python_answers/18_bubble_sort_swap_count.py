# QUESTION
# ---------
# Modify bubble sort to return how many swaps were performed during sorting.
# (Second version: optimise bubble sort by stopping early once the list is sorted.)


def bubblesortcount(lits):
    swap = 0
    for _ in range(len(lits)):
        for i in range(len(lits) - 1):
            if lits[i] > lits[i + 1]:
                temp = lits[i + 1]
                lits[i + 1] = lits[i]
                lits[i] = temp
                swap += 1
    return lits, swap


# i thk can optimise bub sort by stopping when list is sorted
def bubblesortopt(lits):
    swap = 0
    swapped = False
    for _ in range(len(lits)):
        for i in range(len(lits) - 1):
            if lits[i] > lits[i + 1]:
                temp = lits[i + 1]
                lits[i + 1] = lits[i]
                lits[i] = temp
                swap += 1
                swapped = True
        if not swapped:
            break
    return lits, swap


if __name__ == "__main__":
    lits = [6, 5, 4, 3, 2, 1]
    print(bubblesortcount(lits))
    print(bubblesortopt([6, 5, 4, 3, 2, 1]))

# NOTE (review): in bubblesortopt, `swapped` is set once before the outer loop
# and never reset, so after the first swap it stays True and the early break
# never fires. Setting swapped = False at the top of each outer pass fixes it.
