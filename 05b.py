#!/usr/bin/python3
import re
import sys


def find_seat(bpass):
    m = re.match(r"([FB]{7})([LR]{3})", bpass)
    row = int(m.group(1).replace("F", "0").replace("B", "1"), 2)
    column = int(m.group(2).replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column


with open('05.dat') as f:
    lines = f.read()
bpasses = lines.split("\n")
bpasses.pop()
maxid = 0
seat_id_dic = dict()
for bpass in bpasses:
    seat_id = find_seat(bpass)
    seat_id_dic[seat_id] = 1
    if maxid < seat_id:
        maxid = seat_id
for i in range(maxid, 0, -1):
    try:
        seat_id_dic[i] += 1
    except KeyError:
        print(i)
        sys.exit()
