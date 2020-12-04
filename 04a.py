#!/usr/bin/python3


with open('04.dat') as f:
    lines = f.read()
passports = lines.split("\n\n")
valid_fields = ["byr", "iyr", "eyr", "hgt",
                "hcl", "ecl", "pid", "cid"]
valid_field_values = [1, 10, 100, 1000,
                      10000, 100000, 1000000, 10000000]
print('passports:', len(passports))
valid_passports = 0
for passport in passports:
    fields = passport.split()
    total = 0
    for field in fields:
        fid, fval = field.split(':')
        total += valid_field_values[valid_fields.index(fid)]
    if total in [1111111, 11111111]:
        valid_passports += 1
print("Valid passports:", valid_passports)
