# Recursive factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        if n == 0 or n == 1:   # base case
            return 1
        else:                  # recursive case
            return n * factorial(n - 1)

num = int(input("Enter a number: "))

result = factorial(num)
print(f"Factorial of {num} is: {result}")
