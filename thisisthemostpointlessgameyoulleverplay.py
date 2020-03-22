from random import randint as r
question = "Guess my number. It's between ", n1, " and ", n2, "."
n1 = r(0,12489) #random number from 0 to 12489
n1 = r(0,12489)

try:
    while True: #loop endlessly
        try:
            int(input(question)) #ask for a number
        except ValueError: #if they enter text instead of a number
            print("I asked for a number!")
        print("Nope, that's not right.\nGuess again!")
        
except KeyboardInterrupt: #if someone does Ctrl-C
    print(":(")
