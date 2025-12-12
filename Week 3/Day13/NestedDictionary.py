# Work With Nested Dictionaries in Python
students = {}

num = int(input("How many students? "))

for i in range(num):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter student name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    marks = input("Enter marks: ")

    students[name] = {
        "age": age,
        "city": city,
        "marks": marks
    }

print("\nNested Dictionary of Students:")
for student, details in students.items():
    print(student, ":", details)
