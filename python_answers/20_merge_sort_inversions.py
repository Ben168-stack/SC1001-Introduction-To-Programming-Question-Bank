# QUESTION
# ---------
# Merge Sort - Count Inversions
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
# Modify merge sort to count how many inversions are in the list.
#   Example: [3, 1, 2] -> 2 inversions (3 > 1, 3 > 2)
#
# (retry merge sort ugh)


# --- plain merge sort from the previous question, copied here so this file runs
#     on its own. mergesort2 below still calls it, exactly as in the original. ---
def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def mergesort(list):
    if len(list) == 1:
        return list
    mid = len(list) // 2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    return merge(left, right)


# --- the inversion-counting attempt ---
def merge2(left, right):  # comparison of left and right lists
    res = []
    i, j, inversion = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            inversion += len(left) - i
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res, inversion


def mergesort2(list):
    if len(list) == 1:
        return list, 0

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge2(left, right)


if __name__ == "__main__":
    print(mergesort2([5, 1, 4, 2, 8, 3, 6, 7, 0, 23, 324]))

# NOTE (review): mergesort2 recurses into mergesort (the non-counting version),
# so only the inversions found in the final top-level merge get counted - the
# ones inside each half are thrown away. It should call itself, unpack the
# (list, count) tuple from each half, and add all three counts together.
