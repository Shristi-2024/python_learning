# Friday Project: CLI Multi-Tool Program

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

def main():
    while True:
        print("\n--- CLI Multi-Tool ---")
        print("1. Factorial (Recursion)")
        print("2. Fibonacci (Recursion)")
        print("3. Multiplication Table (Loops)")
        print("4. Recursive Sum of N numbers")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == 2:
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == 3:
            n = int(input("Enter number: "))
            multiplication_table(n)

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Recursive Sum:", recursive_sum(n))

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

main()
