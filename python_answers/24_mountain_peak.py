# QUESTION
# ---------
# A "mountain array" increases then decreases.
#   Example = [1, 3, 5, 7, 4, 2]
#   peak is 7
# Use binary search to find the peak index.


def mountain(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:  # mid is on the rising slope still (ie dont search left)
            left = mid + 1
        if arr[mid] > arr[mid + 1]:  # mid is the peak or on falling slope, can ignore right
            right = mid  # ignores right bc we use while left < right.
                         # NOT mid-1 cuz mid could be the peak
    return left  # can return left cuz eventually right == left at the peak yes


if __name__ == "__main__":
    Example = [1, 3, 5, 7, 4, 2]
    print(mountain(Example))
