class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Missing Error")
        self.name = name

class Student(Wizard):    
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Khalil")
student = Student("Harry", "Gryfendio")

professor = Professor("alex", "instructor")