# QUESTION
# ---------
# Search in a Rotated Sorted Array (Binary Search Logic)
#   nums = [5, 6, 7, 1, 2, 3, 4]
#   target = 3 -> index = 5
# You must modify binary search to handle the rotation.


def rotbin(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]

        if arr[left] <= arr[mid]:  # if left half is sorted...
            if arr[left] <= target < arr[mid]:  # target in left
                right = mid - 1
            else:  # target in right
                left = mid + 1

        else:  # if right half is sorted
            if arr[mid] < target <= arr[right]:  # target in right
                left = mid + 1  # search right
            else:
                right = mid - 1  # search left

    return -1


if __name__ == "__main__":
    nums = [5, 6, 7, 1, 2, 3, 4]
    print(rotbin(nums, 3))

# NOTE (review): the question asks for the index, but the hit case returns
# arr[mid] (the value). `return mid` gives the index.
