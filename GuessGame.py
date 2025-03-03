import random

def number_guessing_game():
    try:
        number_to_guess = random.randint(1, 100)
    except Exception as e:
        print(f"Error initializing random number: {e}")
        return
    
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

if __name__ == "__main__":
    number_guessing_game()
