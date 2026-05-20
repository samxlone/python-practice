import random

secret_number = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("Correct! You guessed it 😈")

else:
    print("Wrong number 😭")
    print("The correct number was", secret_number)