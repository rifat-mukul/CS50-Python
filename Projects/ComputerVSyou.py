import random

class Game:

    def __init__(self, n, x) -> None:
        self.n = n
        self.x = x

    def __str__(self) -> str:
        return f"You Win" if True else f"You lose" 
    
    def __gt__(self, other):
        return True if self.n > other.x else False


n = int(input("Enter a number : "))
# x = random.randint(1, n)

print(Game(n, random.randint(1, n)))