# QUESTION
# ---------
# Modify bubble sort so the output is sorted from largest -> smallest.


def bubblesortupsidedown(lits):
    for _ in range(len(lits) - 1):
        for i in range(len(lits) - 1):
            if lits[i] > lits[i + 1]:
                temp = lits[i + 1]
                lits[i + 1] = lits[i]
                lits[i] = temp
    sortlits = lits[::-1]
    return sortlits


if __name__ == "__main__":
    lits = [6, 5, 4, 3, 2, 1]
    print(bubblesortupsidedown(lits))
