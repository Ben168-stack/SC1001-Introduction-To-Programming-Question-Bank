# QUESTION
# ---------
# You get two dictionaries: stock (item -> quantity), order (item -> quantity wanted)
# Return a dictionary of:
#   - items successfully purchased
#   - items insufficient (available stock < ordered)
#
# Example:
#   stock = {'potion': 5, 'elixir': 1, 'bomb': 0}
#   order = {'potion': 3, 'bomb': 1, 'elixir': 2}


def potionshop(stock, order):
    pass


if __name__ == "__main__":
    stock = {'potion': 5, 'elixir': 1, 'bomb': 0}
    order = {'potion': 3, 'bomb': 1, 'elixir': 2}
    print(potionshop(stock, order))
    # edge case: item in stock but not ordered
    print(potionshop({'potion': 5, 'rope': 2}, {'potion': 1}))
