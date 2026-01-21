# TUPLE OPERATIONS

# Concatenating tuples : you can concatenate two or more tuples using +

coordinates = (37.7749, -122.4194)
meta_data = ('Latitude', 'Longitude')
full_data = coordinates + meta_data
print(full_data)

# Repeating tuples : You can multiply tuples with * to repeat its elements
repeated_tuple = (1,2) * 3
print(repeated_tuple)

#slicing tuples: tuples allow slicing just as lists do

tuple_data = (1, 2, 3, 4, 5)
sliced = tuple_data[1:3]
print(sliced)

reversed_data = tuple_data[::-1]
print(reversed_data)

# Counting elements: you can use count() method to see how many times a particular element appears in a tuple
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))

# Iteratiom: you would use a for loop to iterate over a tuple

for label in meta_data:
    print(f'Data label: {label}')


# Sorting tuples
t1 = (4, 3, 10)
print(sorted(t1)) # Since tuples are immutable and cannot be change, this returns a sorted list

## When working with tuples avoid unnecessary conversions to lists as this can increase memory usage and processing time