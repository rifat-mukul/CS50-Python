def main():

    hnumber = int(input("Enter the height number of the palindrom : "))

    Pdom(hnumber)

def Pdom(number):

    count = 1

    i = 0

    while True:

        if count <= number:

            for j in range(i + 1):

                print(count , end=" ")

                count += 1

            i += 1
            print()

        else:
            break
        


main()