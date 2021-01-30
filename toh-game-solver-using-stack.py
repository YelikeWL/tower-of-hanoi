'''Tower of Hanoi game solver (using stack)

Tower of Hanoi game objective is to move the entire stack to another rod,
obeying the following rules:
1. Only 1 disk can be moved at a time.
2. Only move the uppermost disk and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.'''

class ListStack:
    
    def __init__(self, symbol):
        self.data = list()
        self.symbol = symbol

    def is_empty(self):
        return len(self.data) == 0

    def push(self,e):
        self.data.append(e)

    def top(self):
        return self.data[len(self.data) - 1]

    def pop(self):
        return self.data.pop()

def movement(rod_One, rod_Two):
    if rod_One.is_empty():
        rod_One.push(rod_Two.pop())
        print(rod_Two.symbol, "-->", rod_One.symbol)
    elif rod_Two.is_empty():
        rod_Two.push(rod_One.pop())
        print(rod_One.symbol, "-->", rod_Two.symbol)
    elif rod_Two.top() < rod_One.top():
        rod_One.push(rod_Two.pop())
        print(rod_Two.symbol, "-->", rod_One.symbol)
    else:
        rod_Two.push(rod_One.pop())
        print(rod_One.symbol, "-->", rod_Two.symbol)

def HanoiTower(n):
    rod_A = ListStack("A")
    rod_B = ListStack("B")
    rod_C = ListStack("C")

    min_moves = (2 ** n) - 1

    # Stacking in ascending order of size
    for obj in range(n, 0, -1):
        rod_A.push(obj)

    if n % 2 == 0:      # for even number of n the pattern is twisted
        rod_B, rod_C = rod_C, rod_B

    for i in range(min_moves):
        if i % 3 == 0:
            movement(rod_A, rod_C)
        if i % 3 == 1:
            movement(rod_A, rod_B)
        if i % 3 == 2:
            movement(rod_B, rod_C)

while True:
    n = input("Please enter the number of Hanoi's disks: ")
    try:
        n = int(n)
        if n == 0:
            print("Hanoi Tower contain no disk.")
        else:
            HanoiTower(n)
        break
    except ValueError:
        print("Inappropiate input.")
        continue
