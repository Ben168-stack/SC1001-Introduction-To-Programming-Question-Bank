# QUESTION
# ---------
# N is a big number, K is a single digit integer from 0-9.
# Find the sum of specific digits of N, where the condition is that the index
# of the digits must be a multiple of K.
# If the sum is NOT a single digit, repeat the 2nd step recursively on the sum
# until the sum becomes a single digit.
#
# Two variants to try:
#   loop / looprecursive   - N is replaced by the running sum each round
#   loop2 / loop2recursive - N stays the same each round
#
# Watch out for K = 0.


def loop(n, k):
    pass


def loop2(n, k):
    pass


def looprecursive(n, k):
    pass


def loop2recursive(n, k, res=None):
    pass


if __name__ == "__main__":
    print('Change N, no recursion:', loop(9876543210, 2))
    print('Keep N same, no recursion:', loop2(9876543210, 2))
    print('Change N, recursion:', looprecursive(1034489941, 1))
    print('Same N, recursion:', loop2recursive(9876543210, 2))
