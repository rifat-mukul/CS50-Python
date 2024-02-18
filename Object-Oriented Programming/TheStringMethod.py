class Student:
    def __init__(self, name, house, course) -> None:
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Savar", "Dhamrai", "Dhaka", "CTG"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.course = course

    def __str__(self) -> str:
        return f"{self.name} is from {self.house}"
    
    def charm(self):
        match self.course:
            case 220:
                return "repeat"
            case 221:
                return "This is ok"
            case _:
                return "No course"

def main():
    student = get_Student()
    print(student)
    print("Expected course")
    print(student.charm())

    
def get_Student():
    name = input("name : ")
    house = input("house : ")
    course = int(input("Courses : "))
    return Student(name, house, course)


if __name__ == "__main__":
    main()