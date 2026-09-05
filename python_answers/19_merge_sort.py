# QUESTION
# ---------
# Write your own recursive merge sort that returns a new sorted list.


def merge(left, right):
    # 2 lists
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


if __name__ == "__main__":
    print(mergesort([5, 1, 4, 2, 8, 3]))

# NOTE (review): base case is len == 1, so mergesort([]) recurses forever.
# `if len(list) <= 1` covers the empty case.
