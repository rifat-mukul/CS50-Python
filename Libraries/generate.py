from random import choice

def main():

    print(coin())

def coin():
    return choice(["heads", "Tails"])

main()