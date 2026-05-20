def calculate_average(numbers):

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return average


marks = [85, 90, 78]

result = calculate_average(marks)

print("Average is:", round(result, 2))