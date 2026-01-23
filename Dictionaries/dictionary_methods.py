# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATIN, .GET(), .KEYS(), AND .VALUES()

# Assignment and Copying : when you assign one dictionary to another, both variables will refer to the same memory address. no copy is created.

model_params = {'layers': 24, 'units': 512, 'activation': 'relu' }
shared_params = model_params # any channge to shared params will also affect model params as they point to the same memory address

model_params['activation'] = 'gelu'
print(shared_params) # shared params was also changed

#to avoid this we use the copy method
safe_params = model_params.copy()
model_params['layers'] = 48
print(safe_params)

# The upadate() method for merging dictionaries
base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 12}
base_config.update(version_config)
print(base_config)

# clearing Dictionaries with clear()
model_params.clear()
print(model_params) # becareful as this deletes everything in a dictionary

# Dictionary Views with Keys(), values(), and items(): these methods are essential for accessing certain aspects of a dictionary

# keys(): returns all keys in the dictionary
print (base_config.keys())

# values(): gives you a view of all values
print (base_config.values())

#items(): returns both keys and values as tuples making iteration easier

for key, value in base_config.items():
    print(f'{key} => {value}')


# Test membership of specific keys or values with in 
print('learning_rate' in base_config) 


# To remove items from a dictionary you use the following

# dict.pop(key): removes they key and returns the value the key points to. if its not there, it raises an error unless a default return value is specified.
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
age = data.pop('age')
print(age,data)

#to avoid errors with pop, provide a second argument which is a default value and ensures no error is thrown
print(data.pop('country', "Not found"))

# dict.popitem(): removes and returns the last inserted key-value pair as a tuple
last_item = data.popitem()
print(last_item, data)

#del dict[key] #deletes a specific key-value pair from a dictionary, if the key is missing, it raises a keyerror

del data['city']
print(data)

# Set Operations with Dictionary Keys and Items: dictionary keys and items act like sets allowing you to perform set operations on them

config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

common_keys = config_a.keys() & config_b.keys()
print(common_keys)

# Iterating over keys, values and Items

#iterate over keys
for key in base_config.keys():
    print(f'key: {key}')

#iterate over values
for value in base_config.values():
    print(f'value: {value}')    

#iterate over both
for key, value in base_config.items():
    print(f'{key} => {value}')   