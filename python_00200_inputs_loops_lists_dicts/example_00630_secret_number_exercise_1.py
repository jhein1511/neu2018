# Modify the secret number game code below such, that it shows the number of attempts
# after each failed attempt

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
