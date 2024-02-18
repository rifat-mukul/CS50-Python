name = input("Enter the name : ")

match name:

    # idea 1
    # case "Harry":
    #     print("Gryffindoor")

    # case "Hermoine":
    #     print("Gryffindoor")

    # case "Ron":
    #     print("Gryffindoor")

    # case "Draco":
    #     print("Slytherin")

    # case _:
    #     print("Who")

    # idea 2

    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindoor")

    case "Draco":
        print("Slytherin")

    case _:
        print("Who")