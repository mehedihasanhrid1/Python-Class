import random

print("=" * 40)
print("Welcome to Number Hunter!")
print("=" * 40)
print("Instructions:")
print(" - Guess a number between 1 and 10.")
print(" - You have 5 attempts to guess the correct number.")
print(" - Each correct guess earns you 10 points.")
print(" - If you guess incorrectly, you lose 5 points.")
print(" - If you run out of attempts, the game ends.")
print(" - Type 'score' to check your current score.")
print(" - Type 'quit' or 'exit' to end the game anytime.")
print(" - Try to guess the secret number to win!")
print("=" * 40)

secret_number = random.randint(1, 10)
attempts = 0
score = 0

while True:
    user_input = input("Enter your guess (1-10), 'score' to check score, or 'quit' to exit: ").strip().lower()
    
    if user_input in ['quit', 'exit']:
        print("Thanks for playing! Your final score is:", score)
        break
    elif user_input == 'score':
        print("Your current score is:", score)
        continue
    
    try:
        guess = int(user_input)
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    attempts += 1
    
    if guess == secret_number:
        score += 10
        print(f"Correct! You've earned 10 points. Current score: {score}")
        print("=" * 40)
        print("\n")
        secret_number = random.randint(1, 10)
        attempts = 0
        continue
    
    elif guess < secret_number:
        score -= 5
        print(f"Wrong guess! The secret number is higher. You've lost 5 points. Current score: {score}")
        
    elif guess > secret_number:
        score -= 5
        print(f"Wrong guess! The secret number is lower. You've lost 5 points. Current score: {score}")
    
    if attempts >= 5:
        print("You've used all your attempts. The secret number was:", secret_number)
        print("Game over! Your final score is:", score)
        break
    
    else:
        print(f"You have {5 - attempts} attempts left.")
        print("Keep guessing!")
        print("=" * 40)
        continue
    

       


