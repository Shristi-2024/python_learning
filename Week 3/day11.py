# Merge two dictionaries and sum common keys
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged = {key: dict1.get(key, 0) + dict2.get(key, 0)
          for key in set(dict1) | set(dict2)}

print("Merged Dictionary:", merged)


#Merge Two Dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged = {key: dict1.get(key, 0) + dict2.get(key, 0)
          for key in set(dict1) | set(dict2)}

print("Merged Dictionary:", merged)


#CRUD on Lists
numbers = [10, 20, 30, 40, 50]
print("\nInitial List:", numbers)

# Read
print("Reading List:")
for num in numbers:
    print(num)

# Update
numbers[2] = 35
print("After Update:", numbers)

# Delete
numbers.remove(40)
print("After Delete:", numbers)

#List Comprehension Filtering
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

greater_than_25 = [num for num in numbers if num > 25]
print("Numbers > 25:", greater_than_25)

