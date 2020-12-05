from puzzles.utils import resources
import re

with open('input_day4.txt', 'r') as file:
    passports = []
    f = file.read().split('\n\n')
    for line in f:
        passports.append(line.split())

keys_input = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def check_passport(keys_input):
    result = 0

    for passport in range(0, len(passports)):
        keys = []
        is_ok = True
        for element in range(0, len(passports[passport])):
            key = ''
            for i in range(0, len(passports[passport][element])):
                key = key + passports[passport][element][i]
                if i == 2:
                    keys.append(key)
        if len(keys) == len(keys_input):
            result += 1
        elif len(keys) == (len(keys_input) - 1):
            for i in keys:
                if i == 'cid':
                    is_ok = False
            if is_ok == True:
                result += 1
        print(keys)
    return result


print(check_passport(keys_input))
