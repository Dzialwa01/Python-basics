# What is a tuple?

# A Python tuple is an ordered sequence of items. It is immutable, unlike lists
# Immutability can be an advatage especially when creating reliable applications
# The immutability is also memory efficient

# Tuples are mostly used for data that you would not want to change, e.g. coordinates. Storing the data in tuples keeps the data safe and efficient

# To create a tuple you use parentheses with items separated by commas
#e.g

location = (37.7749, -122.4194)

# to create an empty tuple, you can use the tuple() function or just use empty parenthesis

empty_tuple1 = tuple()
empty_tuple2 = ()

print(location)

# creating a single element tuple can be a bit tricky. You need to put a comma after the item, otherwise python assumes a regular value

single = (10,) # this is a tuple
a = (10) # this is an int

# Tuples can also be formed by using the tuple constructor with a list or a string as an argument

num = tuple([1,2,3])
letters = tuple("hello")

# tuples are ordered like string, so indexing can still be used
#e.g
print(location[0]) # This accesses the first element of the tuple.


# tuple unpacking :  This allows you to assign elements to multiple variables in one line
## usually useful with functions that return multiple values
#e.g

coordinates = (37.7749, -122.4194)
latitude, longitude = coordinates
print(latitude, longitude)

# nested tuples : tuples can also contain other tuples, useful for organising complex data structures such as grids and matrices, It still retains the immutability if tuples

matrix = (
    (1,2,3),
    (4,5,6),
    (67,8,9)
)

print(matrix[1][1])

# Best practices and common pitfalls

## Tuples are immutable, if you try to modify an element in a tuple, python will throw a type error

matrix[1] = (4,7,3)
# This immutability can prevent unexpected bugs in your code because it locks down data you dont want to be altered

## use the in operator when checking for membership in tuples

if (1,2,3) in matrix:
    print ("found")