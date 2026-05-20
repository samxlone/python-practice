students = {
    "Samar": [78, 88, 91],
    "Rahul": [65, 70, 60],
    "Aman": [40, 35, 45],
    "Sakshi": [95, 92, 98],
    "Ali": [55, 61, 58]
}
highest_avg = 0
topper = ""
for name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    if average >= 45:
        print(f"{name} Average: {average:.2f} - Pass")
    else:
        print(f"{name} Average: {average:.2f} - Fail")

    if average > highest_avg:
        highest_avg = average
        topper = name

print(f"Topper: {topper} with an average of {highest_avg:.2f}")