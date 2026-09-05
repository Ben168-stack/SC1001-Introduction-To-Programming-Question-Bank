# QUESTION
# ---------
# Without sorting the entire list, merge two already-sorted lists into one
# sorted list.
# MAJULAHHHHHHHHHHHHHHHHHHHHHHHHHh


def merger(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
        else:
            res.append(l2[j])
    res.extend(l1[i:])
    res.extend(l2[j:])

    return res


if __name__ == "__main__":
    # WARNING: this hangs as written - see the note below before running.
    # print(merger([1, 3, 5], [2, 4, 6]))
    pass

# NOTE (review): neither i nor j is ever incremented inside the while loop, so
# it loops forever appending the same element. The working version of this is
# merge() in 19_merge_sort.py.
