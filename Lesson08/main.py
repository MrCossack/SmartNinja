#x = int(input("Gib eine Zahle ein: \n"))
#y = int(input("Gib eine weiter Zahl ein: "))

#text = "bla"

#print("Das Ergebnis von " + x + " und " + y)

#if x == y:
#    print(text)
#elif x > y:
#    print("Groeßer")
#else:
#    print("bla")

#if x != y:
#    print ("Ungleich")

secret = 5

winner = True
while(winner):
    guess = int(input("Guess the secret number: "))

    if guess == secret:
       print("Congratz")
       winner = False
    elif guess < secret:
       print("That was to low!")
    elif guess > secret:
        print("That was to high")