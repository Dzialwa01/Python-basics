# DICTIONARY BASICS

# A dictionary is an ordered collection of keys:value pairs, separated by commas and enclosed by curly braces
# Modules, classes, objects, and sets are all implemented internally as dictionaries

model_congig = {'model_name': 'GPT-4', 'layers': 48, 'parameters': '175B'}
print(type(model_congig))

# Dictionaries do not use index positions, instead they access values using their unique keys. 
# NOTE: dictionary key must be immutable types, using a mutable key throws an error

hyperparameters = {

    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 'Adam'
} # This structure is ideal for managing data that is frequently accessed and updated during model training

# How to ADD, ACCESS, and MODIFY elements in a dictionary

# You can add a new key value pair by assigning a value to a non-existing key 
hyperparameters['batch_size'] = 64
print(hyperparameters)

# To access values you just use the key in square brackets
print(hyperparameters['learning_rate']) # if key does not exist, this throws an error

# to avoid errors, use the get() method as it allows you to specify a default return value if key is not found
print(hyperparameters.get('momentum', 'Not Specified'))

# Best practices to remember when working with dictionaries:
# 1. Stick to immutable keys
# 2. Avoid dulicate keys
# 3. Use .get() method for safe access

# Dictionaries can also hold other dictionaries

pipeline_config = {
    'GPT-4': {'layers': 48, 'parameters' : '175B', 'attention_heads': 96},
    'BERT': {'layers': 24, 'parameters' : '345M', 'attention_heads': 16}
}

# how to access from nested dictionary
print(pipeline_config['GPT-4'])
print(pipeline_config['GPT-4']['attention_heads'])
