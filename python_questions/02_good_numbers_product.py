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
#   list1 = [303, 5, 12], list2 = [11, 24]
#   Output = 5 * 12 * 303 * 11 = 199980
#
# If there are no Good Numbers in list 1 AND no odd numbers in list 2,
# return -1 instead.


def ispalindrome(x):
    pass


def onetwo(x):
    pass


def good1(list1):
    pass


def good2(list2):
    pass


def ohmygod(res, res2):
    pass


if __name__ == "__main__":
    list1 = [303, 5, 12]
    list2 = [11, 24]
    print(ohmygod(good1(list1), good2(list2)))    # expected: 199980
    print(ohmygod(good1([44444444, 7777]), good2([2, 4])))   # expected: -1 case
