
def print_hello(name="markus", number=2):
    #text = "bla "
    #print(text + str(number))
    return "Hello {0}".format(name)


def sum_of_numbers(number1, number2):
    return number1 + number2


if "__main__" == __name__:
    text = "Hello world"
    print_hello(text)
    print(text)
