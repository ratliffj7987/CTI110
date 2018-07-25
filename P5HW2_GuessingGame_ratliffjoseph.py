# my guessing game uses a loop and askes if you would like to play again
# Date
# CTI-110 P5HW2 - Random Number Guessing Game
# Joseph Ratliff

import random
import sys

secret_number = random.randint(1, 100)
tries = 0
tries_remaining = 5
has_won = False


def test_number(guess_num, tries, tries_remaining, has_won):
    if not guess_num > 0 or not guess_num < 101:
        print("That number is not between 1 and 100.")
        tries -= 1
        tries_remaining += 1

    elif guess_num == secret_number:
        print("Congratulations! You are correct!")
        print("It took you {} tries.".format(tries))
        has_won = True

    elif guess_num < secret_number:
        if tries_remaining > 0:
            print("To low. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("Sorry, but my number was {}".format(random_number))
            print("You are out of tries. Better luck next time.")

    elif guess_num > secret_number:
        if tries_remaining > 0:
            print("To high. You have {} tries remaining.".format(int(tries_remaining)))
        else:
            print("My number was {}".format(secret_number))
            print("You are out of tries. Maybe next time.")
            sys.exit()

    return (tries, tries_remaining, has_won)


def main(random_number, tries, tries_remaining, has_won):
    again = 'y'
    while tries < 5:
        guess = input("Guess a random number between 1 and 100. ")
        tries += 1
        tries_remaining -= 1

        try:
            guess_num = int(guess)
            tries, tries_remaining, has_won = test_number(guess_num, tries, tries_remaining, has_won)

        except:
            print("You'r out of tries!")
            tries -= 1
            tries_remaining += 1

        if has_won:
            break
        again= input('Try Again? (y = yes): ')


main(secret_number, tries, tries_remaining, has_won)
