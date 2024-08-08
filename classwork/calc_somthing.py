'''You are given the following two separate lists:'''

# Use a for loop to combine these two lists into a dictionary called 
# inventory with fruits as the keys and quantity as the values. Feel 
# free to add more to the lists or take two different ones and create 
# a dictionary from them.

#Determine if a list is in a sorted order or not.

# Determine if a list is homogenous (all elements in the list are the 
# same data type). For example, if the given list is my_list = [1, 2, 
# 'string', 4, 5], then the program should print False. You can format 
# the output if you'd like to.

fruits = ['apples', 'bananas', 'oranges']
quantity = [10, 8, 20]

for i in fruits:
    print(i)

for i in quantity:
    print(i)
    inventory = dict(zip(fruits, quantity))
    print(inventory)
    
