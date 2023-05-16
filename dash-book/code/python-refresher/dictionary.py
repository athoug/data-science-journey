# -------- Dictionaries --------
'''
The dictionary is a useful data structure for storing key-value pairs. We define a dictionary in curly brackets, like so:
'''
calories = {'apple': 52, 'banana': 89, 'choco': 546}

print(calories['choco'] > calories['apple'])


'''
The dictionary is a mutable data structure, so you can change it after creation. For instance, you can add, remove, or update existing key-value pairs. Here we add a new key-value pair to the dictionary, storing the information that a cappuccino has 74 calories:
'''
calories['cappu'] = 74
print(calories['banana'] < calories['cappu'])


'''
We use the keys() and values() functions to access all keys and values of the dictionary. Here we check whether the string 'apple' is one of the dictionary keys and the integer 52 is one of the dictionary values.
'''
print('apple' in calories.keys())
print(52 in calories.values())


'''
To access all key-value pairs of a dictionary, we use the dictionary.items() method. In the following for loop, we iterate over each (key, value) pair in the calories dictionary and check whether each value is more than 500 calories. If this is the case, it prints the associated key:
'''
for key, value in calories.items():
    if value > 500:
        print(key)
