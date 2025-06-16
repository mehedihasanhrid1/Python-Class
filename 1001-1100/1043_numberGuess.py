import random

print("Welcome to the Number Guessing game!")
print("Guess the number between 1 to 10")
print("You have 5 attempts per round!")
print("Type 'quit' anytime to exit the game.")

score = 0

while True:
    secretNumber = random.randint(1, 10)
    attempts = 0
    maxAttempts = 5

    while attempts < maxAttempts:
        userInput = input(f"Enter your guess on attempt {attempts + 1} out of {maxAttempts}: ")
        if userInput.lower() == "quit":
            print("You have chosen to quit the game.")
            print(f"Your final score: {score}")
            exit()
        try:
            guess = int(userInput)
        except ValueError:
            print("Invalid input! Please enter a number between 1 to 10.")
            continue

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 to 10")
            continue

        attempts += 1

        if guess < secretNumber:
            print("Too low! Guess again!")
            score -= 5
            print(f"You have {maxAttempts - attempts} attempts left!")
            print(f"Your current score: {score}")
        elif guess > secretNumber:
            print("Too high! Guess again!")
            score -= 5
            print(f"You have {maxAttempts - attempts} attempts left!")
            print(f"Your current score: {score}")
        else:
            print("Congratulations! You have guessed the correct answer!")
            score += 10
            print(f"You have used {attempts} attempts!")
            print(f"Your current score: {score}")
            break

    else:
        print("Game Over! You've used all your attempts.")
        print(f"The correct number was: {secretNumber}")
        print(f"Your final score: {score}")
        break