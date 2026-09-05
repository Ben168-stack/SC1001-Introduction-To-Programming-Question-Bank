# QUESTION
# ---------
# You are given 2 lists. In list 1, Good Numbers are those that satisfy EITHER
# of these 2 criteria:
#   a) the number is a palindrome
#   b) the digit 2 appears in the number EXACTLY once
#
# (5 is a palindrome, 12 contains the digit 2, 303 is a palindrome)
# (221 has 2 different 2's and isn't a palindrome, so it isn't a good number)
#
# Multiply all the Good numbers from list 1 with all the Odd numbers in list 2
# and return the product.
#   (Only odd number in list 2 is 11)
#   Output = 5 * 12 * 303 * 11 = 199980
#
# If there are no Good Numbers in list 1 AND no odd numbers in list 2,
# return -1 instead.


def ispalindrome(x):
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < (len(x) - 1) * 0.5 and j > (len(x) - 1) * 0.5:
        if x[i] == x[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True

# ok or a shorter (but slower) code is  if x == x[::-1]
# ie if x is same as reversed x then it is a palindrome.


def onetwo(x):
    return str(x).count('2') == 1


def good1(list1):
    res = []
    for number in list1:
        if ispalindrome(str(number)) or onetwo(str(number)):
            res.append(number)
    return res


def good2(list2):
    res2 = []
    for number in list2:
        if number % 2 == 1:
            res2.append(number)
    return res2


def ohmygod(res, res2):
    result = 1
    for i in res:
        result *= i
    for j in res2:
        result *= j
    return result


if __name__ == "__main__":
    list1 = [303, 5, 12, 3003, 13569]
    list2 = [11, 23, 24]

    res = good1(list1)
    res2 = good2(list2)

    print(res)
    print(res2)
    print(ohmygod(res, res2))

# NOTE (review): the "return -1 if both lists are empty" rule isn't handled yet.
# ohmygod([], []) currently returns 1.
