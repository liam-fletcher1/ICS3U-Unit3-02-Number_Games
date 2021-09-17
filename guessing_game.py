#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to guess a number between 0 - 9

import constants


def main():
    # this tells the user if they picked the right number

    # input
    random_number = int(input("Enter a number between 0 - 9 : "))

    # process & output
    if random_number == constants.CORRECT_NUMBER:
        print("You guessed the number correctly!")
        print("")
        print("Done.")
    if random_number > constants.CORRECT_NUMBER:
        print("You guessed the number incorrectly :(")
        print("")
        print("Done.")
    if random_number < constants.CORRECT_NUMBER:
        print("You guessed the number incorrectly :(")
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
