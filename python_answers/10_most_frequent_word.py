# QUESTION
# ---------
# Given a list of words, return the word that appears most frequently.
# If tied, return the alphabetically earliest.


def slaydiva(liste):
    wordfreq = {}
    for words in liste:
        wordfreq[words] = wordfreq.get(words, 0) + 1
    maxvalue = max(wordfreq.values())
    freqword = None
    for words in wordfreq:
        if wordfreq[words] == maxvalue:
            if freqword == None or words < freqword:
                freqword = words
    return freqword


if __name__ == "__main__":
    test = ["banana", "apple", "cat", "banana", "dog",
            "apple", "carrot", "banana", "apple"]
    print(slaydiva(test))
