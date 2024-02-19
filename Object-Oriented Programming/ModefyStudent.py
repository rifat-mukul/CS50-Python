class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} is from {self.house}"
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError ("Missing Name")
    #     self._name = name
    
    # #Gatter
    # @property
    # def house(self):
    #     return self._house
    
    # #setter
    # @house.setter
    # def house(self, house):
    #     if house not in ["Savar", "Dhamrai", "Dhaka", "CTG"]:
    #         raise ValueError("invalid House")
    #     self._house = house

    @classmethod
    def get(cls):
        name = input("Name : ")
        house = input("House : ")
        return cls(name, house)
    

def main():
    student = Student.get()
    # student.house = "Gazipur"
    print(student)
    
# def get_Student():
#     name = input("name : ")
#     house = input("house : ")
#     return Student(name, house)


if __name__ == "__main__":
    main()