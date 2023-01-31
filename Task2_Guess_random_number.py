import random

num_to_guess = random.randint(1, 20)

for num in range(3):
    guess = int(input("Guess the number (1-20): "))

    if guess < 1 or guess > 20:
        print("Invalid guess, number must be between 1 and 20.")
    elif guess > num_to_guess:
        print("Too high, try again.")
    elif guess < num_to_guess:
        print("Too low, try again.")
    else:
        print("Correct! You guessed the number in", num + 1, "tries.")
        break
else:
    print("Sadly you didn't guess the number. The number was", num_to_guess)
