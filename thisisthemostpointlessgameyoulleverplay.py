from random import randint as r
from sys import exit
n1 = r(0,12489) #random number from 0 to 12489
n2 = r(0,12489)
exit = False

try:
    while True: #loop endlessly
        try:
            print("Guess my number. It's between ", n1," and", n2, ".")
            int(input("Type: ")) #ask for a number
        except ValueError: #if they enter text instead of a number
            print("I asked for a number!")
            continue
        except KeyboardInterrupt:
            if exit ==  False:
                print("Please don't quit me. It's not nice!")
                exit = True
                continue
            elif exit == True:
                print("\n :(")
                exit()
        print("Nope, that's not right.\nGuess again!")
except KeyboardInterrupt: #if someone does Ctrl-C
    print("\n:(")
except:
    print("An unknown error occured.")
