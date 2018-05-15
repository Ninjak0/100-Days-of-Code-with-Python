import itertools
import time
import random

colours = "Red Green Yellow".split()
rotation = itertools.cycle(colours)

def rg_timer():
    return random.randint(3, 7)

def light_rotation(rotation):
    for colour in rotation:
        if colour == "Yellow":
            print(f"Caution! The light is {colour}")
            time.sleep(3)
        elif colour == "Red":
            print(f"STOP! The light is {colour}")
            time.sleep(rg_timer())
        else:
            print(f"Go! The light is {colour}")
            time.sleep(rg_timer())

if __name__ == '__main__':
    light_rotation(rotation)