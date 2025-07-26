# numericfunctions.py

def approximatePI(n_values):
    sum_of_n_values = 0
    for i in range(n_values):
        if i % 2 == 0:
            sum_of_n_values += 4 / (1 + i * 2)
        else:
            sum_of_n_values -= 4 / (1 + i * 2)
    return sum_of_n_values

def newtonSquareRoot(num):
    pass

def sumN(n_values):
    sum_of_n_values = 0
    for i in range(n_values):
        sum_of_n_values += i + 1
    return sum_of_n_values

def sumNCubes(n_values):
    sum_of_n_cubes = 0
    for i in range(n_values):
        sum_of_n_cubes += (i + 1) ** 3
    return sum_of_n_cubes

