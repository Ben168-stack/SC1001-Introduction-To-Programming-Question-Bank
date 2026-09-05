# QUESTION
# ---------
# Input: a list of words.
# For each word, count how many vowels (a, e, i, o, u) appear exactly once.
# Return the word with the highest count.
# If tied, return the shortest word.


def countvowels(word):
    pass


def highest(list1):
    pass


if __name__ == "__main__":
    list1 = ['a', 'ae', 'aeiou', 'aaee', 'ppp', 'aaeeiioouu']
    print(highest(list1))            # expected: aeiou
    print(highest(['ppp', 'zzz']))   # edge case: no vowels appear once
