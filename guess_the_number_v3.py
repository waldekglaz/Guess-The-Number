import random

from time import sleep

# create the random secret number


def generate_the_number(min, max):
    number = random.randint(min, max)
    return number


def game(number):
    guess = ""
    number_of_guesses_left = 12
    number_of_guesses = 0

    while not(guess == number) or (number_of_guesses_left == 0):
        number_of_guesses_left -= 1
        number_of_guesses += 1
        guess = input("Guess the number between 0 and 100: ")
        if guess == "":
            print("We need a number!")
        if guess > str(number):
            print(
                f"The secret number is lower than {guess}. Number of guesses left: {number_of_guesses_left}")
        elif guess < str(number):
            print(
                f"The secret number is bigger than {guess}. Number of guesses left: {number_of_guesses_left}")
        else:

            print("*" * 5)
            print(
                f"Congratulations {player}! The secret number was {number}. You guessed the number in {number_of_guesses} guesses")
            print("*" * 5)
            sleep(2)
            break
        if number_of_guesses_left == 0:
            print(f"Game Over. You lose! The secret number was {str(number)}")
            sleep(2)
            break


while(True):
    start_game = input("Do you want to start a new game? (Y)es or (N)o? > ")
    if start_game.lower() == "y":
        player = input("What is your name? > ")
        print("Welcome", player)
        game(generate_the_number(0, 100))
    else:
        print("Good Bye!")
        break
