# 1. Sort list of dictionaries
students = [
    {"name": "Riya", "age": 22},
    {"name": "Arjun", "age": 20},
    {"name": "Meera", "age": 21}
]

print("Sorted by age:", sorted(students, key=lambda x: x["age"]))
print("Sorted by name:", sorted(students, key=lambda x: x["name"]))


# 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = list(map(int, input("\nEnter numbers: ").split()))
print("Bubble sorted:", bubble_sort(nums))


# 3. Lambda with collections
numbers = [5, 2, 9, 1, 3]
print("Sorted using lambda:", sorted(numbers, key=lambda x: x))

words = ["apple", "kiwi", "banana", "mango"]
print("Sorted by length:", sorted(words, key=lambda x: len(x)))

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)
