name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course name: ")

student = {
    "name": name,
    "age": age,
    "course": course
}

print("\nDictionary:", student)

print("Student name:", student.get("name"))
print("Keys:", student.keys())
print("Values:", student.values())

print("\nDictionary items:")
for key, value in student.items():
    print(key, ":", value)
