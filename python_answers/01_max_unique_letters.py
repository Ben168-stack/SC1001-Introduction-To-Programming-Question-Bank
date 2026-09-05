# QUESTION
# ---------
# You are given a list of N words.
# Write a function that takes the list of words and calculates the number of
# letters that only appear once in each word.
#   E.g. "Apple" has 3 such letters: A, L, E  (P appears twice and isn't counted)
#
# Return the word that has the highest number of letters that only appear once.
# If multiple words have the same number of such letters, return the one that
# appears first alphabetically.
#   E.g. "Carrot" and "Pear" both have 4 letters that only appear once.
#        Output is "Carrot" because it comes first alphabetically.
#
# ie list1 = [apple, banana, carrot, pear]


def numuniqueletters(x):
    count = {}
    for letter in x.lower():
        count[letter] = count.get(letter, 0) + 1
    return sum(1 for numoccurrences in count.values() if numoccurrences == 1)


def maxunique(listx):
    best = -1
    bestword = None
    for words in listx:
        uniquecount = numuniqueletters(words)
        if uniquecount > best:
            best = uniquecount
            bestword = words
        elif uniquecount == best:
            if words.lower() < bestword.lower():  # alphabetically lower = smaller
                bestword = words
    return bestword


if __name__ == "__main__":
    listx = ['apple', 'banana', 'carrot', 'pear']
    print(numuniqueletters(listx[0]))
    print(maxunique(listx))
