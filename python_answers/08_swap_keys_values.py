# QUESTION
# ---------
# Given a dictionary, return a new dictionary with keys and values swapped.
# If two keys share the same value, store the keys in a list.


def swapvk(dick):
    res = {}
    for key, value in dick.items():
        if value not in res:
            res[value] = [key]
        else:
            res[value].append(key)
    return res


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 1}
    print(swapvk(d))
