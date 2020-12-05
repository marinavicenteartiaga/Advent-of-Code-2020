from puzzles.utils import resources
from puzzles.day_4 import check_methods


def main():

    keys_input = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    with open('input_day4.txt', 'r') as file:
        passports = []
        f = file.read().split('\n\n')
        for line in f:
            passports.append(line.split())

    passports_checked = check_methods.check_passports_parameters(keys_input, passports)
    input_list = resources.input_text_to_list_of_dictionaries(passports_checked)

    print('The number of valid passports is: ', check_methods.check_passports(input_list))


main()
