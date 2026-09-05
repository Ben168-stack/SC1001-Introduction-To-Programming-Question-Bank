# QUESTION
# ---------
# Write a function that uses bubble sort to sort a list of integers in
# ascending order.


def bubblesort(lits):
    for _ in range(len(lits)):
        for i in range(len(lits) - 1):
            if lits[i] > lits[i + 1]:
                temp = lits[i + 1]
                lits[i + 1] = lits[i]
                lits[i] = temp
    return lits


if __name__ == "__main__":
    lits = [6, 5, 4, 3, 2, 1]
    print(bubblesort(lits))
