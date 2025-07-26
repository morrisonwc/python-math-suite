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

