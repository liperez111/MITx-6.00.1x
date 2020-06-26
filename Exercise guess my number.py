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