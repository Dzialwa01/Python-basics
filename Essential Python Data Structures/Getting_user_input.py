# Dzialwa Nemakonde
# 05 December 2025

#GETTING USER INPUT

#Python gathers input with the input() function
#e.g.
command = input('Ask your AI assistant a question: ')
print('Your question was:', command)

# No matter what the user enters, the data is stored as a string. If you need it in another form, you have to convert it
#e.g.
training_hours = input('Enter hours spent training the model: ')
print('Data type of training hours:', type(training_hours))

#common mistake is to forget to convert input into integers before calculations

iterations = int(input('Enter number of iterations: '))
datasets = int(input('Enter number of datasets: '))
total = iterations * datasets
print('Total processing units:', total)