my_dict = {"a": ["hello", 20,'abc'], "b": ["hello2", 20, "dafd"]}
#my_dict = {"a": 1, "b": 2}
my_set = set()
print(my_set)
# Convert dictionary to a frozenset of its items
#my_set.add(frozenset(my_dict.items()))
#print(my_set)

"""
#fset= frozenset(my_set.items())
for key, value in my_set:
    print(f"Key: {key}, Value: {value}")
    """
unique_dicts = []
unique_dicts.append(my_dict)
print(unique_dicts)
for i in unique_dicts:
    for key, item in i.items():
        print(key, item)