# QUESTION
# ---------
# Using linear search only, count how many times a target number appears in a list.
# lowkey still need to consider edge cases like empty list but lets ignore that lol


def linearocc(lis, target):
    count = 0
    for i in range(len(lis)):
        if lis[i] == target:
            count += 1
    return count


if __name__ == "__main__":
    lis = [0, 0, 3, 0, 5, 5, 6, 7, 0]
    print(linearocc(lis, 0))
