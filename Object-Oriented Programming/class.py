class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house

def main():
    student = get_Student()
    print(f"{student.name} is from {student.house}")

    
def get_Student():
    name = input("name ")
    house = input("house ")
    return Student(name, house)


if __name__ == "__main__":
    main()