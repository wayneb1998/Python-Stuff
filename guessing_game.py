secret_number = 13
guess_count = 0
guesses_allowed = 3

while guess_count < guesses_allowed:
    guess = int(input("Guess the secret number: "))
    guess_count += 1
    if guess == secret_number:
        print("You are correct!")
        break
else:
    print("Sorry, you were incorrect, run the code to try again :)")

