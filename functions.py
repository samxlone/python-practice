def welcome(name):
    print("Welcome", name)
    print("Hope you enjoy coding 😈")
welcome( input("Enter your name: ") )

def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a, b)

print("The result is:", result)