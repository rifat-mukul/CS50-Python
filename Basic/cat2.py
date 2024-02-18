def main():

    number = getNumber()

    print(Meow(number))


def getNumber():

    while True:
        n = int(input("ENTER A NUMBER : "))

        if n > 0:
            return n
        

def Meow(n):

    x = ""

    for _ in range(n):
        x += "meow "

    return x

main()