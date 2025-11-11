import random


random_number = random.randint(1, 6)
a = input("IN THIS GAME YOU HAVE ONE CHANCE TO GUESS A NUMBER BETWEEN 1-6 AND IF YOU GUESS WRONG YOURE SYSTEM WILL BE ERASED (joke) !!! PRESS ENTER TO START THE GAME OR CTRL+C TO EXIT IM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS GAME ") 
if a == "":
    print(""" 
 R R R R R R R       U             U        S S S S S S S       R R R R R R R     U             U       L                E E E E E E E           T T T T T T T
 R             R     U             U       S                  R             R     U             U       L                E                             T
 R             R     U             U       S                  R             R     U             U       L                E                             T
 R R R R R R R       U             U       S S S S S S S S    R R R R R R R       U             U       L                E E E E E E E                 T
 R        R          U             U                     S    R        R          U             U       L                E                             T
 R            R      U             U                     S    R            R      U             U       L                E                             T
 R             R      U U U U U U U        S S S S S S S S    R             R      U U U U U U U        L L L L L        E E E E E E E                 T
""")
while True:
    guess = (input('ONE CHANCE 1-6: '))
    try:
        guess = (guess)
    except ValueError:
        print("UNVALID INPUT: please enter an integer or CTRL + C  to quit.")
    if 0 <= guess <= 6:
        print("PLEASE ENTER A VALID NUMBER BETWEEN 1-6")
    if guess == random_number:
        print("YOU LOST! and your system shouldve been erased but im a troll :D  so your system is safe")
        break
    else:
        print("YOU WON!")
