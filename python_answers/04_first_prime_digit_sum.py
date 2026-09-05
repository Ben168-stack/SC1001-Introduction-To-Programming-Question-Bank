# QUESTION
# ---------
# Input: a list of integers.
# For each number, calculate the sum of its digits.
# Return the first number whose digit-sum is prime.
# If none exist, return -1.


def checkprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def idek(leest):
    for integer in leest:
        sum = 0
        for number in str(integer):
            sum += int(number)
        if checkprime(sum):
            return integer
    return -1


if __name__ == "__main__":
    list1 = [10, 22, 35, 99, 101, 123, 88, 41, 77, 56]
    print(idek(list1))
