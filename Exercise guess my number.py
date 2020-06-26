#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses,
#and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
#Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
#When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input.


a = 100
b = 0
c = int(a / 2)
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(c) + "?")
n = input(
    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while n != "c":
    if n not in ["h", "l", "c"]:
        while n not in ["h", "l", "c"]:
            print("Sorry, I did not understand your input.")
            print("Is your secret number " + str(c) + "?")
            n = input(
                "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if n == "l":
        b = c
        e = (a - c) / 2
        c = int(b + e)
        print("Is your secret number " + str(c) + "?")
        n = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if n not in ["h", "l", "c"]:
            while n not in ["h", "l", "c"]:
                print("Sorry, I did not understand your input.")
                print("Is your secret number " + str(c) + "?")
                n = input(
                    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif n == "h":
        a = c
        e = (a - b) / 2
        c = int(b + e)
        print("Is your secret number " + str(c) + "?")
        n = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if n not in ["h", "l", "c"]:
            while n not in ["h", "l", "c"]:
                print("Sorry, I did not understand your input.")
                print("Is your secret number " + str(c) + "?")
                n = input(
                    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret number was: " + str(c))