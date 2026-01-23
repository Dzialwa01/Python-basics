# SSET BASICS

# What is a set? -> An unordered collection of unique immutable elements
## Each element in a set is distinct. Duplicates are automatically removed

# In python we define a set using curly braces and separate elements with a commma

unique_ids = {1, 2, 3, 'a', 'b', 4} # sets  elements of different immutable types

# sets are unordered and as a result you cannot use indexing with them

print(unique_ids) # elements can also be printed in a different order

# To create an empty set, use the set constructor, as using empty curly braces will create a dictionary instead (print(type({})))

empty_set = set()

# You can easily convert other sequence types, i.e lists, tuples and strings, to sets. Handy when you want to remove duplicates

sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
unique_sentences = set(sentences)
print(unique_sentences)


# FROZENSETS -> these are immutable sets. Once created you cannot add or remove elements from it
# They are useful when you need a set that need to remain constant in your program.

immutable_tokens = frozenset(unique_ids)

# A set  utilizes a hash table for storage, allowing for average-case constant time complexity for lookups, making it the fastest among the given options.