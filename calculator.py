def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation (1/2/3/4): ")

if choice == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", add(num1, num2))

elif choice == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", subtract(num1, num2))

elif choice == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", multiply(num1, num2))

elif choice == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        print("Cannot divide by zero 😭")

    else:
        print("Result:", divide(num1, num2))

else:
    print("Invalid choice 😭")