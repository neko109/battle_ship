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

ships = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
}

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
        
        if is_valid_position(x, y, length, orientation) == True:
            for i in range(length):
                if orientation == 'horizontal':
                    used_cells.add((x + i, y))
                    if length == 1:
                        ships["1"].append((x + i, y))
                    elif length == 2:
                        ships["2"].append((x + i, y))
                    elif length == 3:
                        ships["3"].append((x + i, y))
                    else:
                        ships["4"].append((x + i, y))
                    ax.add_patch(plt.Rectangle((x + i, y), 1, 1, color='black'))
                else:
                    used_cells.add((x, y + i))
                    if length == 1:
                        ships["1"].append((x, y + i))
                    elif length == 2:
                        ships["2"].append((x, y + i))
                    elif length == 3:
                        ships["3"].append((x, y + i))
                    else:
                        ships["4"].append((x, y + i))
                    ax.add_patch(plt.Rectangle((x, y + i), 1, 1, color='black'))
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

def check_hit(x, y):
    for length, positions in ships.items():
        if (x, y) in positions:
            hit_cells.add((x, y))
            positions.remove((x, y))
            if not positions:
                print(f"Ship with length {length} destroyed!")
            else:
                print("Shot!")
            return True
    print("Miss!")
    return False

def game(ax, ships):
    while ships:
        x = int(input("Input X value (0-9): "))
        y = int(input("Input Y value (0-9): ")) 
        if (x, y) in hit_cells:
            print("You already hit this cell")
        elif check_hit(x, y):
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='red'))
        else:
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='blue'))
        plt.draw()
        plt.pause(0.5)

    print("Game over! All ships are destroyed")

game(ax1, ships)

print(ships)

plt.show()