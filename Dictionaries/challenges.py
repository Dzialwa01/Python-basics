# Dzialwa Nemakonde
# 26 January 2026

# Challenge #1

# Write a Python script that removes all duplicate elements from a list in a single line using sets.

def unique(lists):
    list1 = set(lists)
    print (list1)

#********************************************************************************************
# Challenge #2

# Write a Python script that counts and displays the occurrences of each character in a list.

def occurences (sentence):

    list1 = list(sentence)
    keys = []

    for i in list1:
        if i not in keys:
            keys.append(i)

    diction = {}
    for i in keys:
        diction[i] = list1.count(i)
    print(diction)
               

occurences('mamma mia mm')   

# Example:
# Input: list('mamma mia mm')
# Output:

# m ---> 6
# a ---> 3
# ---> 2
# i ---> 1

#********************************************************************************************


# Challenge #3

# Given a list of words, write a Python script that creates a dictionary where each word is a key, and its length is the value.

def dictionary_maker(words):

    dict1 = {}

    for word in words:
        dict1[word] = len(word)

    print(dict1)    

dictionary_maker( ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash'])
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

#********************************************************************************************

# Challenge #4

# Considering the following dict, get a dict representation sorted by key.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

for k in sorted(d1.keys()):
    print(f"{k} -> {d1[k]}")

#********************************************************************************************

# Considering the following dict, get a dict representation sorted by value.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

view = sorted(d1.items(), key = lambda x: x[1]) # key = lambda x: tells sorted what to sort by; and each x is a tuple so x[1] means use the value (not the key) for sorting 
# The lambda is a short way form to create a function without a name. It says take x and return x[1]
print(view)

