from abc import ABC, abstractmethod
class vehicle(ABC):
    #abstract base class for vehicle
    def __init__(self,n) -> None:
        self.no_of_type=n

    @abstractmethod
    def start(self):
        #abstract method to start the vehicle
        pass

class Bike:
    #class representing a bike

    def __init__(self) -> None:
        self.no_of_tyres = 2
    def start(self):
        #method to start the bike 
        print("start with kick")

class Scooty:
    #class representing a scooty

    def __init__(self) -> None:
        self.no_of_tyres = 2
    def start(self):
        #method to start the scooty
        print("selfstart")

class Car:
    def __init__(self) -> None:
        self.no_of_tyres = 4
    def start(self):
        print("start with key")

v = vehicle