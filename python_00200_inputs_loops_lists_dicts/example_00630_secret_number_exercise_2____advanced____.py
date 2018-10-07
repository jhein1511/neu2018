# Modify the secret number game, such that errors are caught when the users inputs not convertible strings

secret = 7
guess = None

while True:
    guess = raw_input("Guess the secret number")
    guess = int(guess)

    if guess == secret:
        print "Oh, so great!, you won!"
        break
    else:
        print "Oh no, please try again."
