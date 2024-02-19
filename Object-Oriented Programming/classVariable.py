import random
class Hat:
    house = ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))

Hat.sort("Harry")