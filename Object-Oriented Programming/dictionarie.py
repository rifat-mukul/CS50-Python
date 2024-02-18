def main():
    student = get_Student()
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} is from {student['house']}")

    
def get_Student():
    name = input("Name : ")
    house = input("house : ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()