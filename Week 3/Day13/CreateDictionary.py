# Create a Dictionary from User Input
n = int(input("How many key-value pairs do you want to add? "))

user_dict = {}

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    user_dict[key] = value

print("\nYour Dictionary:")
print(user_dict)
