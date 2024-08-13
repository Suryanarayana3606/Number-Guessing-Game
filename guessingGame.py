import random

def number_guessing_game():
    target_number = random.randint(1,101)
    print(f"Guess the number between 1 to 100")
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def main():
    number_guessing_game()

if __name__ == "__main__":
    main()