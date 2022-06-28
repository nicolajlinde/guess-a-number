import random
import art

# Start of functions
def attempt():
    global LIVES
    number = int(input("Guess a number between 1-100: "))

    if number > rnd_num:
        print("The number is too high")
        LIVES -= 1
    elif number < rnd_num:
        print("The number is too low")
        LIVES -= 1
    elif number == rnd_num:
        print(f"GUESS WHAT? YOU WON! THE SECRET NUMBER WAS {rnd_num}")
        LIVES = 0
    elif LIVES == 0:
        print("YOU DIED")


# End of functions
# Scopes
rnd_num = random.randint(1, 100)

print(art.logo)
print(f"Welcome to 'Guess What?'\nWhere you have to guess a number between 1-100\n")

print(f"Psst, the secret number is: {rnd_num}")

# Variables
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff == "easy":
    LIVES = 10
    while LIVES != 0:
        attempt()
elif diff == "hard":
    LIVES = 5
    while LIVES != 0:
        attempt()

