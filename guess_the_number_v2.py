import random
# random number
number = random.randint(0, 100)
guess = ""
number_of_guesses_left = 5
# loop over till guess == number or number_of_guesses_left
while not(guess == str(number) or number_of_guesses_left == 0):
    number_of_guesses_left -= 1
    guess = input("Guess the number between 0 and 100: ")

    if guess > str(number):
        print(
            f"secret number is lower than {guess}. Number of guesses left: {number_of_guesses_left}")
    elif guess < str(number):
        print(
            f"The secret number is bigger than {guess}. Number of guesses left: {number_of_guesses_left}")
    else:
        print("*")
        print(
            f"Congratulations! The secret number was {number}. You guessed the number is {5+1 - number_of_guesses_left} guesses")
        print("*")
    #

    if number_of_guesses_left == 0:
        print(f"Game Over. You lose! The secret number was {str(number)}")
