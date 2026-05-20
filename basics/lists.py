numbers = [4, 7, 2, 9, 1]

print(numbers)
print(numbers[0])
print(numbers[3])
numbers.append(100)

print(numbers)
numbers.insert(0, 999)

print(numbers)
numbers.remove(7)

print(numbers)

for num in numbers:
    if num % 2 == 0:
        print("Even:", num)
    else:
        print("Odd:", num)