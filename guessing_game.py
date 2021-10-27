secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess_count += 1
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("Yes, you win, you have used " + str(guess_count) + " tries")
    else: 
        print("Keep trying, you are on your " + str(guess_count) + " guess, out of " + str(guess_limit))
