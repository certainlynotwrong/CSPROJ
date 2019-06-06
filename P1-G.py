# This is a guess the number game.
import random

guessesTaken = 0
print('What range of numbers would you like to guess from? Enter the first number, follwed by [Enter], and repeat for the second number')
first = int(input())
second = int(input())

number = random.randint(first, second)
print('Well, I am thinking of a number between ' + str(first) + ' and ' + str(second) + '.')


print('How many guesses would you like to be able to take?')
chosen = input()
print('Okay, you can take ' + chosen + ' guess(es)')
while guessesTaken < int(chosen):
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
