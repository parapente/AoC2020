#!/usr/bin/python3
import sys

with open('01.dat') as f:
    lines = f.read()
nums = lines.split("\n")
nums.pop()
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if (int(nums[i]) + int(nums[j])) == 2020:
            print(int(nums[i]) * int(nums[j]))
            sys.exit()
