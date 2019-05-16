import random
from Lesson13.BasketballPlayer import BasketballPlayer

moritz = BasketballPlayer("Moritz", "Test", 455, 543, 445)
print(moritz.first_name)

number = 8
number2 = 8.4
text = "text"
condition = True

menu = ["Schnitzel", "Gulasch", 3.4]
map = {"Austria": "Vienna", "France": "Paris"}

print(map["Austria"])


def print_to_console():
    print ("Hello")


for item in menu:
    print(item)

print_to_console()

