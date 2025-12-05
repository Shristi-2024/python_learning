# Find nth Fibonacci number using recursion
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the position (n): "))

print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
