import random
# random number
number = random.randint(0, 100)
guess = ""
number_of_guesses = 0
# loop over till guess == number
while guess != str(number):

    guess = input("Guess the number between 0 and 100: ")

    if int(guess) > number:
        number_of_guesses += 1
        print(
            f"secret number is lower than {guess}. Number of guesses: {number_of_guesses}")
    elif int(guess) < number:
        number_of_guesses += 1
        print(
            f"The secret number is bigger than {guess}. Number of guesses: {number_of_guesses}")
    else:
        print("*")
        print(
            f"Congratulations! The secret number was {number}. You guessed it in {number_of_guesses + 1} guesses")
        print("*")
