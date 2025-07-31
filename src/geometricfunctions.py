# geometricformulas.py
import math

def sphereVolume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume

def sphereSurfaceArea(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

def slopeOfALine(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

def distanceBetweenPoints(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def triangleArea(side_a, side_b, side_c):
    semiperimeter = (side_a + side_b + side_c) / 2
    area = math.sqrt(semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c))
    return area

def quadraticFormula(value_a, value_b, value_c):
    disc_root = math.sqrt(value_b * value_b - 4 * value_a * value_c)
    root1 = (-value_b + disc_root) / (2 * value_a)
    root2 = (-value_b - disc_root) / (2 * value_a)
    return root1, root2
