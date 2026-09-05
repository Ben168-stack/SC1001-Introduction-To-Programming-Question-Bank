# QUESTION
# ---------
# Sort a list of dictionaries (e.g. students with name and score) using merge
# sort, based on:
#   primary key:   score (descending)
#   secondary key: name (alphabetically ascending)


def sortstudents(students):
    pass


if __name__ == "__main__":
    students = [
        {"name": "carrie", "score": 88},
        {"name": "alice", "score": 92},
        {"name": "bob", "score": 88},
        {"name": "dan", "score": 95},
    ]
    print(sortstudents(students))
    # expected order: dan 95, alice 92, bob 88, carrie 88
