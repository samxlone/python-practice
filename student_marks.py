marks = {
    "Math": 85,
    "Physics": 90,
    "Chemistry": 78
}

total = 0

for subject in marks:
    print(subject, ":", marks[subject])
    total += marks[subject]

print("Total marks:", total)