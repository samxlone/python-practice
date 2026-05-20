import random

secret_number = random.randint(1, 10)

attempts = 3

while attempts > 0:

    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct 😈")
        break

    else:
        attempts -= 1
        print("Wrong 😭")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over 💀")
    print("The number was", secret_number)