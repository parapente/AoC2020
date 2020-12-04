#!/usr/bin/python3


with open('03.dat') as f:
    lines = f.read()
area = lines.split("\n")
area.pop()
maxy = len(area)
maxx = len(area[0])
crashes = 0
pos = [0, 0]
while pos[1] < maxy:
    if area[pos[1]][pos[0]] == '#':
        crashes += 1
    pos[0] = (pos[0] + 3) % maxx
    pos[1] += 1
print('Crashes:', crashes)
