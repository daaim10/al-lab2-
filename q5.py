
# Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five.
# Sample list of strings
words = ["Apple", "Banana", "Grape", "Strawberry", "Watermelon", "Orange"]

# List comprehension to generate lowercased version of strings with length greater than five
lowercased_long_words = [word.lower() for word in words if len(word) > 5]

# Printing the result
print("Lowercased version of strings with length greater than five:", lowercased_long_words)


# )Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']
# Sample list
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

# Removing 0th, 4th, and 5th elements using list slicing
modified_list = sample_list[1:4] + sample_list[6:]

# Printing the modified list
print("Modified list:", modified_list)
