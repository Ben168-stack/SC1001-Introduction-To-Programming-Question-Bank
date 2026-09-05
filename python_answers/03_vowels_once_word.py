# QUESTION
# ---------
# Input: a list of words.
# For each word, count how many vowels (a, e, i, o, u) appear exactly once.
# Return the word with the highest count.
# If tied, return the shortest word.


def countvowels(word):
    vowels = 'aeiou'
    res = 0
    for letter in vowels:
        if word.count(letter) == 1:
            res += 1
    return res


def highest(list1):
    bestword = None
    bestcount = 0
    for word in list1:
        count = countvowels(word)
        if count > bestcount:
            bestword = word
            bestcount = count
        elif count == bestcount:
            if len(word) < len(bestword):
                bestcount = count
                bestword = word
    return bestword


if __name__ == "__main__":
    list1 = ['a', 'ae', 'aeiou', 'aaee', 'ppp', 'aaeeiioouu']
    print(highest(list1))

# NOTE (review): if the first word scores 0, the elif branch runs len(bestword)
# while bestword is still None -> TypeError. Try highest(['ppp', 'apple']).
