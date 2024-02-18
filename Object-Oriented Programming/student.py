def main():
    # name = get_Name()
    # house = get_house()
    name, house = get_Student()
    print(f"{name} is from {house}")

# def get_Name():
#     return input("Name : ").capitalize()

# def get_house():
#     return input("House : ")
    
def get_Student():
    return (input("Name ").capitalize(), input("House "))

if __name__ == "__main__":
    main()