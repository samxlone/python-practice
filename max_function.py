def find_largest(numbers):

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


my_list = [4, 7, 2, 9, 1]

answer = find_largest(my_list)

print("Largest number is:", answer)