# Dzialwa Nemakonde
# 08 December 2025

# F-Strings with = for debugging

name , age = 'Alice', 30
print(f'Your name is {name} and you are {age} years old.')

# Sometimes, this might not output the right thing and you might want to debug and see the value of your variables
# We can use f string with =
#e.g.
print(f'Your name is {name=} and you are {age=} years old.')

r = 13.3
PI = 3.141592
print(f'Circle area with a radius of {r=} is {PI * r ** 2=}')
# You can still use standard formatting options within the debugging process
print(f'Circle area with a radius of {r=} is {PI * r ** 2=:.3f}')

## f-string with = are a powerful addition to the debugging toolkit which makes it easy to inspect variables and expressions