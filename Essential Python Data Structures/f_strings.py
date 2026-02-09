# Dzialwa Nemakonde
# 08 December 2025

# FORMATTED STRINGS: USING F-STRINGS FOR CLEAN OUTPUT

model_name = 'GPT'
version = 4
print('Hello from ' + model_name + '-' + str(version) + '!')

# This approach required changing version to a string and manually managing each part of the sentence
# With f strings we can achieve the same outcome in a cleaner and readable way

#e.g.
print(f'Hello from {model_name}-{version}!')
# f allows us to add variables in curly braces within a string, no matter the type of the variable

# f strings are also useful for evaluating expressions
token_used = 123
cost_per_token = 0.001
total_cost = f'{token_used * cost_per_token:.4f}' #:.4f shows that we want 4 decimal places
print(f'Total cost for this message: {total_cost}')