# 1. Write a Python function that takes two dictionaries as input and returns a new dictionary containing all key-value pairs from both dictionaries. If a key exists in both dictionaries, the value from the second dictionary should be used.

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

d1 = {'a': 100, 'b': 250}
d2 = {'b': 150, 'c': 430}
print(merge_dicts(d1, d2))


