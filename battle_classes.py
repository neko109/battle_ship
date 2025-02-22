import matplotlib.pyplot as plt
from matplotlib import colors
import random 
from random import randint

# инициализировать поле
# обработать ход

class Field:
    def __init__(self, position_left = True):
        self.position_left = position_left
        self.cells = []
        self.ships = []
        for i in range(10):
            for j in range(10):
                cell = Cell(i, j)
                self.cells.append(cell)
    def print_cells(self):
        for cell in self.cells:
            print(f'[{cell.x},{cell.y}] - {'occupied' if cell.occupied else 'empty'}, {'hit' if cell.hit else 'not hit'}')
    def find_cell_by_xy(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
    def is_valid_position(self, x, y, length, orientation):
        used_cells = []
        for cell in self.cells:
            if cell.occupied:
                used_cells.append((cell.x, cell.y))
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

        # algorithm to place a ship

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
                #ship_positions = []
                for i in range(length):
                    if orientation == 'horizontal':
                        cell = self.find_cell_by_xy(x + i, y)
                        #вот здесь сразу делать оккупай всех соседних клеток
                        cell.occupy()
                        ship.add_cell(cell)
                        #ax.add_patch(plt.Rectangle((x + i, y), 1, 1, color='white'))
                    else:
                        cell = self.find_cell_by_xy(x, y + i)
                        cell.occupy()
                        ship.add_cell(cell)
                        #ax.add_patch(plt.Rectangle((x, y + i), 1, 1, color='white'))
                self.ships.append(ship)
                placed = True
            attempts += 1

        # здесь мы должны выдать кораблю клетки
        # но не забыть что клетка не выдана другому кораблю и не соседняя с выданным кораблю
        ship.add_cell(cell)
        self.ships.append(ship)
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
        for cell in self.cells:
            pass
            

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
MyField.place_ship(3)
MyField.place_ship(3)
MyField.place_ship(4)
MyField.print_cells()


s = Ship(4)
s.add_cell(1,1)
s.add_cell(1,2)
s.add_cell(1,3)
s.add_cell(1,4)

#field_left.cells[0] (0, 0)

#field_left.ships[3].cell[0] (0, 0)

#field_left = Field(position_left = True)
#field_right = Field(position_left = False)

#field_left.place_ships()
#field_right.place_ships()
#field_left.show()
#field_right.show()