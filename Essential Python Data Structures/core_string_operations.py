# Dzialwa Nemakonde
# 08 December 2025

#CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

# A string in python has indexes of all characters which starts from 0
#e.g.
message = 'GenAI is amazing!'

#to access a character, we use square brackets.
print(message[0])
print(message[6])

#Python also lets us use negative indices to count backwards
# The last char has index -1 the second last had index -2 and so on
#e.g.
print(message[-1])  #= !

#If you index something beyond the range of a string it will give you an error
#To avoid this we can use the len() function to get the length of the string ensuring we stay within bounds
n = len(message)
print(message[n-1])

#Python strings are immutable so we cannot make direct changes to characters
#To change we need to create a new string


# concatenation
# We use '+' to join two strings

greeting = 'Hello, '
role = 'AI enthusiast'
print(greeting + role + '!')

# You can't concatenate a string with a number directly
# You need to convert the number to a string first using 'str()'

#To repeat strings we use the * operator
seperator = 'Dzialwa'
print(seperator * 5)


#Slicing
#This allows us to grab a range of characters known as a substring within a string
#Syntax for slicing -> String[start:stop] it stops before the stop index (it is exclusive)
#e.g.
tech = 'Machine learning'
print(tech[0:7])

#if you omit, start -> 0, stop -> end of string
#slicing does not give an error even if range for slicing is beyond the length of the string

#we can also have a third argument called step: string[start:stop:step]
#It allows us to skip characters

print(tech[0:14:2])

#to reverse a string, just put step as -1
print(tech[::-1])