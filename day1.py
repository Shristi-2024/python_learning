# Reverse a String without Slicing
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("My name is Shristi Kumari"))