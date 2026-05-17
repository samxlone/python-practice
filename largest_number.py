numbers = [4, 7, 2, 9, 1]
numbers.append(int(input("Enter number: ")))

print(numbers)
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)