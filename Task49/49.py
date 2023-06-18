import random
from math import pi

def find_farthest_orbit(list_of_orb: list) -> tuple:
    dict_ = {round(pi * orbit[0] / 2 * orbit[1]/2, 2): orbit for orbit in 
             filter(lambda orbit: orbit[0] != orbit[1], list_of_orb)}
    return dict_

num = int(input('Введите список планет: '))
orbits = [(random.randint(1,10), random.randint(1,10)) for _ in range(num)]
dict_p = find_farthest_orbit(orbits)
print(dict_p)
print(max(dict_p), dict_p[max(dict_p)])