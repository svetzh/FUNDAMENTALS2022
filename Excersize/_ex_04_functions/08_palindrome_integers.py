import random
from sty import fg


def generate_RBB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue


def generate_color(red, green, blue):
    return fg(red, green, blue)


red, green, blue = generate_RBB()
color = generate_color(red, green, blue)
print(color, "Changed color")
