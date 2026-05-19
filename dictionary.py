student = {
    "name": "John",
    "age": 18,
    "course": "Python"
}

print(student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

student["age"] = 19
student["city"] = "Kolkata"

print(student)

for key in student:
    print(key, ":", student[key])