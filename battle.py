import matplotlib.pyplot as plt
from matplotlib import colors
import random 
from random import randint

x = random.randint(0, 9)
y = random.randint(0, 9)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

def draw_grid(ax):
    for i in range(11):
        ax.plot([i, i], [0, 10], color='black')
        ax.plot([0, 10], [i, i], color='black')

draw_grid(ax1)
draw_grid(ax2)

used_cells = set()

def is_valid_position(x, y, length, orientation):
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

ships = []
def place_ship(ax, length):
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
        
        if is_valid_position(x, y, length, orientation):
            ship_positions = []
            for i in range(length):
                if orientation == 'horizontal':
                    used_cells.add((x + i, y))
                    ship_positions.append((x + i, y))
                    ax.add_patch(plt.Rectangle((x + i, y), 1, 1, color='white'))
                else:
                    used_cells.add((x, y + i))
                    ship_positions.append((x, y + i))
                    ax.add_patch(plt.Rectangle((x, y + i), 1, 1, color='white'))
            ships.append(ship_positions)
            placed = True
        attempts += 1


place_ship(ax1, 4)

place_ship(ax1, 3)
place_ship(ax1, 3)

place_ship(ax1, 2)
place_ship(ax1, 2)
place_ship(ax1, 2)

place_ship(ax1, 1)
place_ship(ax1, 1)
place_ship(ax1, 1)
place_ship(ax1, 1)

hit_cells = set()

def mark_surroundings(ax, ship_cells):
    print(ship_cells)
    surrounding_cells = set()
    for x, y in ship_cells:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in hit_cells and (nx, ny) not in used_cells:
                    surrounding_cells.add((nx, ny))
    print(surrounding_cells)
    for nx, ny in surrounding_cells:
        ax.add_patch(plt.Rectangle((nx, ny), 1, 1, color='blue'))
        hit_cells.add((nx, ny))


def check_hit(x, y, ax):
    global ships
    for ship in ships:
        if (x, y) in ship:
            hit_cells.add((x, y))
            ship.remove((x, y))
            print(ship)
            if len(ship) == 0:
                print(f"Ship destroyed!")
                mark_surroundings(ax, ship)
                ships.remove(ship)
                print(ship)
            else:
                print("Shot!")
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='red'))
            return True
    print("Miss!")
    ax.add_patch(plt.Rectangle((x, y), 1, 1, color='blue'))
    return False

def game(ax, ships):
    while ships:
        while True:
            try:
                x = int(input("Input X value (0-9): "))
                y = int(input("Input Y value (0-9): "))
                if x < 0 or x > 9 or y < 0 or y > 9:
                    raise ValueError()
                break
            except ValueError:
                print("Invalid input")
        if (x, y) in hit_cells:
            print("You already hit this cell")
        elif check_hit(x, y, ax1):
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='red'))
        else:
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='blue'))
        plt.draw()
        plt.pause(0.5)

    print("Game over! All ships are destroyed")

game(ax1, ships)

print(ships)

plt.show()