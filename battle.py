import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random

class Field:
    def __init__(self, position_left=True):
        self.position_left = position_left
        self.cells = []
        self.ships = []
        for i in range(10):
            for j in range(10):
                cell = Cell(i, j)
                self.cells.append(cell)
    
    def print_cells(self):
        for cell in self.cells:
            print(f'[{cell.x},{cell.y}] - {"occupied" if cell.occupied else "empty"}, {"hit" if cell.hit else "not hit"}')
    
    def find_cell_by_xy(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
    
    def is_valid_position(self, x, y, length, orientation):
        used_cells = [(cell.x, cell.y) for cell in self.cells if cell.occupied]
        for i in range(length):
            if orientation == 'horizontal':
                if (x + i, y) in used_cells:
                    return False
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (0 <= x + i + dx < 10) and (0 <= y + dy < 10) and (x + i + dx, y + dy) in used_cells:
                            return False
            else:
                if (x, y + i) in used_cells:
                    return False
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (0 <= x + dx < 10) and (0 <= y + i + dy < 10) and (x + dx, y + i + dy) in used_cells:
                            return False
        return True
    
    def place_ship(self, length):
        ship = Ship(length)
        placed = False
        attempts = 0
        while not placed and attempts < 10000:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 10 - length)
                y = random.randint(0, 9)
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 10 - length)
            
            if self.is_valid_position(x, y, length, orientation):
                for i in range(length):
                    if orientation == 'horizontal':
                        cell = self.find_cell_by_xy(x + i, y)
                    else:
                        cell = self.find_cell_by_xy(x, y + i)
                    cell.occupy()
                    ship.add_cell(cell)
                self.ships.append(ship)
                placed = True
            attempts += 1
    def check_hit(self, x, y):
        for ship in self.ships:
            for cell in ship.cells:
                if x == cell.x and y == cell.y:
                    cell.hit = True
                    for cell in ship.cells:
                        if cell.hit == False:
                            pass
                            #корабль ранен, но еще жив
                        else:
                            pass
                            #корабль убит
                            #не забыть поменять статус соседних клеток
        #мимо
    
    def show(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks(range(11))
        ax.set_yticks(range(11))
        ax.grid(True)

        for cell in self.cells:
            rect = Rectangle((cell.x, cell.y), 1, 1, facecolor='black' if cell.occupied else 'white')
            ax.add_patch(rect)
            if cell.hit:
                ax.add_patch(Rectangle((cell.x, cell.y), 1, 1, color='red'))

        
        plt.show()

class Ship:
    def __init__(self, length):
        self.cells = []
        self.length = length - 1
    def add_cell(self, cell):
        if len(self.cells) > self.length:
            pass
            #raise ValueError(f'The ship has already reached its max size')
        self.cells.append(cell)
        cell.occupy()

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False
        self.hit = False
    def occupy(self):
        if self.occupied:
            pass
            #raise ValueError(f'Cell [{self.x},{self.y}] is already used')
        self.occupied = True


MyField = Field()
MyField.place_ship(1)
MyField.place_ship(1)
MyField.place_ship(1)
MyField.place_ship(1)
MyField.place_ship(2)
MyField.place_ship(2)
MyField.place_ship(2)
MyField.place_ship(3)
MyField.place_ship(3)
MyField.place_ship(4)
MyField.show()
