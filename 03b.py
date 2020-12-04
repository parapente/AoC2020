#!/usr/bin/python3
from functools import reduce


def check_slope(right, down):
    crashes = 0
    pos = [0, 0]
    while pos[1] < maxy:
        if area[pos[1]][pos[0]] == '#':
            crashes += 1
        pos[0] = (pos[0] + right) % maxx
        pos[1] += down
    return crashes


with open('03.dat') as f:
    lines = f.read()
area = lines.split("\n")
area.pop()
maxy = len(area)
maxx = len(area[0])
res = [check_slope(1, 1), check_slope(3, 1), check_slope(5, 1),
       check_slope(7, 1), check_slope(1, 2)]
print(reduce((lambda x, y: x*y), res))
