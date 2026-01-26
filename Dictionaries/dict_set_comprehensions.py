# SET AND DICTIONARY COMPREHENSIONS

# Set Comprehensions

names = {'alice', 'BOB', 'charlie','DAVE'}
formatted_names = {name.capitalize() for name in names} # This is useful when we want consistency in our data
print(formatted_names)

# Dictionary comprehensions
hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}
adjusted_params = {k: v*2 for k, v in hyperparams.items()} 
print(adjusted_params) # we simply doubled the values for each key

updated_params = {k.upper() for k, v in hyperparams.items() if v > 0.2}
print(updated_params)

#using the zip() function for pairing data. It extremly useful for pairing data in two different lists into a dictionary
years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]
data_growth = dict(zip(years, dataset_sizes))
print(data_growth)

#another example
sales = {2022: 50000, 2023: 75000, 2024: 100000}
profit = {year: revenue * 0.15 for year, revenue in sales.items()}
print(profit) #calculates the profit in just one line making the code clean

