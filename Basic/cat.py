def main():

    print(Cat(3))

def Cat(number):

    x  = ""

    #if you need a variable just because the programing feature ew
    #require but 
    # if you dont care about the value then just use an Underscore[_]

    for _ in range(number):
        x += "meow "

    return x
    
main()

print("meow " * 3) # not best but smart practice
print("meow\n" * 3, end="") # not best but smart practice