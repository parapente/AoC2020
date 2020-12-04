#!/usr/bin/python3


def check_policy(policy, password):
    minmax, letter = policy.split()
    minmax = minmax.split('-')
    if (password[int(minmax[0])] == letter) ^ (password[int(minmax[1])] == letter):
        return True
    return False


with open('02.dat') as f:
    lines = f.read()
passdb = lines.split("\n")
passdb.pop()
total = 0
for line in passdb:
    policy, password = line.split(':')
    if check_policy(policy, password):
        total += 1
print("Valid passwords:", total)
