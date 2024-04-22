#
# Example implementation of some dictionary functions

# 1. Creating an empty dictionary
my_dict = {}

# 2. Adding key-value pairs using 'update'
my_dict.update({'a': 1, 'b': 2, 'c': 3})
print("Updated dictionary:", my_dict)

# 3. Accessing values using 'get'
value = my_dict.get('b')
print("Value associated with key 'b':", value)

# 4. Removing a key-value pair using 'pop'
removed_value = my_dict.pop('a')
print("Removed value associated with key 'a':", removed_value)
print("Dictionary after removing key 'a':", my_dict)

# 5. Checking if a key exists using 'in'
if 'c' in my_dict:
    print("Key 'c' exists in the dictionary.")

# 6. Getting a list of keys using 'keys'
keys = my_dict.keys()
print("Keys in the dictionary:", keys)

# 7. Getting a list of values using 'values'
values = my_dict.values()
print("Values in the dictionary:", values)

# 8. Getting a list of key-value pairs using 'items'
items = my_dict.items()
print("Key-value pairs in the dictionary:", items)

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating a new dictionary by concatenating the sample dictionaries
result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

# Printing the concatenated dictionary
print("Concatenated dictionary:", result_dict)
