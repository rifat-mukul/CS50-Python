import random

def main():

    print(Number())

def Number():

    return random.randint(1, 6)

n = int(input("Enter a number : "))
x = random.randint(1, n)

main()