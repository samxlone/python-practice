students = {
    "John": [85, 90, 78],
    "Adnan": [70, 88, 92],
    "Alex": [95, 99, 91]
}

for name in students:
    marks = students[name]

    total = 0

    for num in marks:
        total += num

    average = total / len(marks)

    print(name, "got average:", round(average, 2))