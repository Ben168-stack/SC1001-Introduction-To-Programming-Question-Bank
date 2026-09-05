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
    purchased = {}
    insufficient = {}
    for key in stock:
        stork = stock[key]
        orde = order[key]
        if stork < orde:
            insufficient[key] = orde - stork
        elif stork >= orde:
            purchased[key] = orde
    return purchased, insufficient


if __name__ == "__main__":
    stock = {'potion': 5, 'elixir': 1, 'bomb': 0}
    order = {'potion': 3, 'bomb': 1, 'elixir': 2}
    print(potionshop(stock, order))

# i mean this is def like shit for actual game implementation cuz i didnt add
# the part where stock changes when you purchase but oh well...
#
# NOTE (review): order[key] raises KeyError if an item is in stock but not ordered.
# order.get(key, 0) would handle that.
