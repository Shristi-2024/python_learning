# a Demonstrate Tuple Immutability
elements = input("Enter tuple elements separated by space: ").split()
t = tuple(elements)

print("Your tuple:", t)

try:
    index = int(input("Enter index to modify: "))
    value = input("Enter new value: ")
    t[index] = value   # This will cause an error
except TypeError as e:
    print("Error:", e)
except IndexError:
    print("Invalid index!")
