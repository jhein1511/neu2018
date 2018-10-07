# Modify the secret number game, such that errors are caught when the users inputs not convertible strings

secret = 7
guess = None

while True:
    while True:
        try:
            guess = raw_input("Guess the secret number")
            guess = int(guess)
            break
        except ValueError:
            print "You did not enter a number"

    if guess == secret:
        print "Oh, so great!, you won!"
        break
    else:
        print "Oh no, please try again."
