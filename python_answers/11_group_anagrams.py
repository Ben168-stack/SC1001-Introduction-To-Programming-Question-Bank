# QUESTION
# ---------
# Given a list of words, group them into lists of anagrams.
#   test = ["eat", "tea", "ate", "bat", "tab"]


def anagrams(lit):
    res = {}
    for word in lit:
        sorte = ''.join(sorted(word))
        if sorte not in res:
            res[sorte] = [word]
        else:
            res[sorte].append(word)
    return res


if __name__ == "__main__":
    test = ["eat", "tea", "ate", "bat", "tab"]
    print(anagrams(test))
