def square(num):
    return num * num

nums = [2, 5, 8, 11, 14]
for num in nums:
    if num % 2 == 0:
        print(num, "is an even number.")

student = {
    "name": "Sajid",
    "marks": 89
}
print(f'{student["name"]} scored {student["marks"]}')

print(square(5))