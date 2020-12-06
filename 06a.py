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
            answers[c] = 1
    group_answers += len(answers)
    answers.clear()
print(group_answers)
