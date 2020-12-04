#!/usr/bin/python3
import re


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
        ok = False
        if fid == "byr" and (1920 <= int(fval) <= 2002):
            ok = True
        if fid == "iyr" and (2010 <= int(fval) <= 2020):
            ok = True
        if fid == "eyr" and (2020 <= int(fval) <= 2030):
            ok = True
        if fid == "hgt":
            m = re.match(r"^(\d+)(.+)$", fval)
            if m:
                if len(m.groups()) == 2:
                    if (m.group(2) == "cm") and (150 <= int(m.group(1)) <= 193):
                        ok = True
                    if (m.group(2) == "in") and (59 <= int(m.group(1)) <= 76):
                        ok = True
        if fid == "hcl":
            m = re.match(r"^#[0-9a-f]{6}$", fval)
            if m:
                ok = True
        if fid == "ecl":
            if fval in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                ok = True
        if fid == "pid":
            m = re.match(r"^\d{9}$", fval)
            if m:
                ok = True

        if ok:
            total += valid_field_values[valid_fields.index(fid)]
    if total in [1111111, 11111111]:

        valid_passports += 1
print("Valid passports:", valid_passports)
