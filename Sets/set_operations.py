# SET OPERATIONS AND METHODS

# sets are important as they insure there are no unnecessary duplicates in data

unique_ids = {1, 2, 3, 1} 
print(unique_ids) # when we try to add duplicates, the set removes it

# sets themselves are mutable, meaning you can add and remove elements after the set has been defimed

# to add an element you use the add() method and to remove you use the remove() method

unique_ids.add('a')
print(unique_ids)

unique_ids.remove('a')
print(unique_ids)

# NB: remember, sets must contain immutable elements, if you try to add mutable elemets, you obtain a type error

unique_ids.add([1,2,3,4])

# You can iterate over a set using a for loop, however the elements will come out in no particular order

# to check the availability of an element in a set, you can use the in and not in 3operators