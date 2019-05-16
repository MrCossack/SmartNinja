import random
#from random import randint

secret = random.randint(0, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())

score_file.close()
print("Old Highscore: " + str(best_score))

while True:
    attempts += 1
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

if attempts < best_score:
    with open("score.txt", "w") as score_file:
        score_file.write(str(attempts))
    score_file.close()

