#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nicol
#
# Created:     21/12/2021
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint

logo = '''
 [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
 /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /
       |____________|____________|____________|____________|
                             |            |            |
                         ___  \_      ___  \_      ___  \_
                        [(_)] |=|    [(_)] |=|    [(_)] |=|
                         '-`  |_|     '-`  |_|     '-`  |_|
                        /mmm/        /mmm/        /mmm/              '''


print(logo)


print("Welcome to the Guess Number Game!")
print("I am thinking at a number between 1 and 100 .... ")
#ask1 = input("Are you ready to play? (yes/no): ").lower()





def easy_way():
       num_select = randint(1,100)
       print(f"Psssst, the number computer chooses is {num_select}")
       guess = None
       tryAgain = True
       lives = 10
       guess = int(input("Guess the number: "))
       while guess != num_select:
        if guess < num_select:
            print("Too low. Try again!")
            lives -= 1
            print(f"You have left {lives} lives ")
        else:
            print("Too high. Try again!")
            lives -= 1
            print(f"You have left {lives} lives ")
        guess = int(input("Guess the number: "))
        if guess == num_select:
            print(f"Congratulations! You have guessed the number! It was {num_select}")
            break
        if lives == 0:
            print(f"You lose. The number chosen by the computer was {num_select}")
            break


def hard_way():
       num_select = randint(1,100)
       print(f"Psssst, the number computer chooses is {num_select}")
       guess = None
       tryAgain = True
       lives = 5
       guess = int(input("Guess the number: "))
       while guess != num_select:
        if guess < num_select:
            print("Too low. Try again!")
            lives -= 1
            print(f"You have left {lives} lives ")
        else:
            print("Too high. Try again!")
            lives -= 1
            print(f"You have left {lives} lives ")
        guess = int(input("Guess the number: "))
        if guess == num_select:
            print(f"Congratulations! You have guessed the number! It was {num_select}")
            break
        if lives == 0:
            print(f"You lose. The number chosen by the computer was {num_select}")
            break




def main():
    selection = input("Select wich game difficulty you want to play (easy/hard): ").lower()
    if selection == "easy":
        easy_way()
    else:
        hard_way()


if __name__ == '__main__':
    main()
