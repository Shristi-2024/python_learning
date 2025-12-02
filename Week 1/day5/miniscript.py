
def compound_interest(P, r, t, n):
    """Calculate compound interest"""
    return P * (1 + r/n)**(n*t)

# --- Hello World + Variables ---
print("Hello, this is my python practice learning")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.\n")

# --- Reverse a string without slicing ---
word = input("Enter a word to reverse: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(f"Reversed word: {reversed_word}\n")

# --- Check if two strings are anagrams ---
s1 = input("Enter first string for anagram check: ").lower()
s2 = input("Enter second string: ").lower()
if sorted(s1) == sorted(s2):
    print("The strings are anagrams!\n")
else:
    print("The strings are not anagrams.\n")

# --- Format user input into a sentence ---
city = input("Enter your city: ")
print(f"{name} is {age} years old and lives in {city}.\n")

# --- Calculate compound interest ---
P = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): ")) / 100
t = int(input("Enter time in years: "))
n = int(input("Enter compounding frequency per year: "))

final_amount = compound_interest(P, r, t, n)
CI = final_amount - P

print("\n--- Compound Interest Result ---")
print(f"Final Amount after {t} years: {final_amount:.2f}")
print(f"Compound Interest earned: {CI:.2f}")
