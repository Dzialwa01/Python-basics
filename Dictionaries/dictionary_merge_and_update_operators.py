# Dictionary merge (|) and update (|=) operators

# the merge operator allows you to combine two dictionaries into a new dictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2 # this operator combines the values and keys from both dictionaries. If there are overlapping keys, the values of the right hand side dict will overwrite the values of the left hand side dictionary

print(merged_dict)

# this operator is useful when you want to combine dictionaries without modifying the original ones

# update operator -> this operator updates the left dictionaries with the values and keys of the right dictionary. A short hand from the update() method
dict1 |= dict2
print(dict1)