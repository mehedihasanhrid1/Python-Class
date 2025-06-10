import random

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    try:
        lower = get_int_input("Enter the lower bound: ")
        upper = get_int_input("Enter the upper bound: ")
        if lower >= upper:
            raise ValueError("Lower bound must be less than upper bound.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    try:
        secret = random.randint(lower, upper)
    except Exception as e:
        print(f"Error generating secret number: {e}")
        return

    attempts = 0
    while True:
        try:
            guess = get_int_input(f"Guess a number between {lower} and {upper}: ")
            attempts += 1
            if guess < lower or guess > upper:
                raise IndexError("Guess out of bounds!")
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except IndexError as ie:
            print(f"Error: {ie}")
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def save_score(attempts):
    try:
        with open("scores.txt", "a") as f:
            f.write(f"Attempts: {attempts}\n")
    except FileNotFoundError:
        print("Score file not found. Creating a new one.")
        with open("scores.txt", "w") as f:
            f.write(f"Attempts: {attempts}\n")
    except PermissionError:
        print("Permission denied: Cannot write to score file.")
    except Exception as e:
        print(f"Error saving score: {e}")

if __name__ == "__main__":
    try:
        play_guessing_game()
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        print("Thank you for playing!")