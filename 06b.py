#!/usr/bin/python3


with open('06.dat') as f:
    lines = f.read()
groups = lines.split("\n\n")

group_answers = 0
answers = dict()
for group in groups:
    pass_ans = group.split()
    for ans in pass_ans:
        for c in ans:
            try:
                answers[c] += 1
            except KeyError:
                answers[c] = 1
    for key, val in answers.items():
        if val == len(pass_ans):
            group_answers += 1
    answers.clear()
print(group_answers)
