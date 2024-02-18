def main():

    number = int(input("Enter a number : "))

    if is_even(number):
        print("The number is even")

    else:
        print("Enter the numbner is odd")


def is_even(number):

    # idea 1

    # if number % 2 == 0:
    #     return True
    
    # else:
    #     return False

    # ============

    # idea 2
    
    # return True if number % 2 == 0 else False 

    # ============

    # idea 3

    return number % 2 == 0

    # ============
    

main()