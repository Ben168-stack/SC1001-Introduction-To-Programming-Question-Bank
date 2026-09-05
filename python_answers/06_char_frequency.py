# QUESTION
# ---------
# Write a function that takes a string and returns a dictionary mapping each
# character to the number of times it appears, ignoring case.


def abcd(st):
    st = st.lower()
    res = {}
    for char in st:
        if char not in res:
            res[char] = 1
        elif char in res:
            res[char] += 1
    return res


if __name__ == "__main__":
    print(abcd("baNAnA"))
