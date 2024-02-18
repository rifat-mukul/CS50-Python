import random

def main():

    card = ["Jack", "Queen", "King"]

    print(Number(card))

def Number(card):

    random.shuffle(card)

    x = ""

    for i in card:
        x += i+ " "

    return x


main()