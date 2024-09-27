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

# NOTES
# Struggled a little bit with the "break" - forgot to indent the print command after the IF statement
# Otherwise pretty easy and little to no errors
# Source: https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PL2YqTZEeE8_lWnyeLl3_YNxkddUXvx3cU&index=5 
