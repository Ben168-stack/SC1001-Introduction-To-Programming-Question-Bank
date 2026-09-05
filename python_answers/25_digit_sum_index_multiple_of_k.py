# QUESTION
# ---------
# N is a big number, K is a single digit integer from 0-9.
# Find the sum of specific digits of N, where the condition is that the index
# of the digits must be a multiple of K.
# If the sum is NOT a single digit, repeat the 2nd step recursively on the sum
# until the sum becomes a single digit.
#
# ok wait so... first add digits, then check if its single digit. if not,
# repeat function.
#
# This file holds all four attempts:
#   loop()            - iterative, N is replaced by the running sum
#   loop2()           - iterative, N stays the same
#   looprecursive()   - recursive, N is replaced by the running sum
#   loop2recursive()  - recursive, N stays the same (incomplete)


def loop(n, k):
    n = str(n)
    res = 0
    singledigit = False
    while singledigit == False:
        for i in range(len(n)):
            if i % k == 0:  # if index is multiple of k then add the digit
                res += int(n[i])
                print(res)
        if len(str(res)) == 1:
            singledigit = True
        else:
            n = str(res)
            res = 0
    return res


# ok new one where n stays the same
# so uh put n digits divisible by k into a list
# then first sum those digits
# if res not single digit, sum digits that are in the dictionary
def loop2(n, k):
    digits = []  # list of n digits with index divisible by k
    n = str(n)
    res = 0
    singledigit = False
    while singledigit == False:
        for i in range(len(n)):
            if i % k == 0:
                digits.append(int(n[i]))
        for j in range(len(digits)):
            if str(digits[j]) in n:
                res += digits[j]
        if len(str(res)) == 1:
            singledigit = True
        else:
            n = str(res)
            res = 0
    return res


# recursive, changing n
def looprecursive(n, k):
    n = str(n)
    if len(n) == 1:
        return n
    gooddigits = [int(n[i]) for i in range(len(n)) if i % k == 0]

    res = sum(gooddigits)

    return looprecursive(res, k)


def loop2recursive(n, k, res=None):
    n = str(n)
    if res == None:
        gooddigits = [int(n[i]) for i in range(len(n)) if i % k == 0]
        res = sum(gooddigits)

    if res < 10:
        return res

    res2 = sum(int(d) for d in res)

    return loop2recursive(n, k, res)


if __name__ == "__main__":
    # print(loop(9876543210, 2))
    print('Keep N same, no recursion:', loop2(9876543210, 2))
    print('Change N, recursion:', looprecursive(1034489941, 1))
    # print('Same N, recursion:', loop2recursive(9876543210, 2))

# NOTES (review):
# - k = 0 breaks every version (i % 0 -> ZeroDivisionError), even though the
#   question allows K from 0-9.
# - looprecursive returns a string (n) from the base case but an int elsewhere.
# - loop2recursive has two problems: `sum(int(d) for d in res)` iterates over an
#   int (TypeError), and res2 is computed but never passed on, so the recursive
#   call repeats with the same res forever.
