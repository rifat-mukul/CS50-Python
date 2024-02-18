

def main():
    name = input("ENter your name : ")

    hello() #without argument

    hello(name) #with argument

def hello(to = "World"):
    print("hello", to)

main()