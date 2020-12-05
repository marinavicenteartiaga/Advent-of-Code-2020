def check_passports_parameters(keys_input, passports):
    result = 0
    passports_checked = []

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
            passports_checked.append(passports[passport])
        elif len(keys) == (len(keys_input) - 1):
            for i in keys:
                if i == 'cid':
                    is_ok = False
            if is_ok == True:
                result += 1
                passports_checked.append(passports[passport])
    return passports_checked


def check_birth_year(byr):
    if 2020 >= int(byr) >= 1920:
        return True


def check_issue_year(iyr):
    if 2020 >= int(iyr) >= 2010:
        return True


def check_expiration_year(eyr):
    if 2030 >= int(eyr) >= 2020:
        return True


def check_height(hgt):
    if hgt[len(hgt)-2] == 'c' and hgt[len(hgt)-1] == 'm':
        value = hgt[0:len(hgt)-2]
        if 193 >=int(value) >= 150:
            return True
    if hgt[len(hgt) - 2] == 'i' and hgt[len(hgt) - 1] == 'n':
        value = hgt[0:len(hgt) - 2]
        if 76 >= int(value) >= 59:
            return True


def check_hair_color(hcl):
    for i in hcl:
        if hcl[0] == '#' and len(hcl) == 7:
            for j in range(1, len(hcl)):
                if j != range(0, 9) or j != 'a' or j != 'b' or j != 'c' or j != 'd' or j != 'e' or j != 'f':
                    return True


def check_eye_color(ecl):
    hair_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for i in range(0, len(hair_colors)):
        if ecl == hair_colors[i]:
            return True


def check_pid(pid):
    if len(pid) == 9:
        return True


def check_passport_parameters(key):
    is_ok = True
    if key == 'byr':
        is_ok = check_birth_year('byr')
    elif key == 'eyr':
        is_ok = check_expiration_year('eyr')
    elif key == 'iyr':
        is_ok = check_issue_year('iyr')
    elif key == 'hgt':
        is_ok = check_height('hgt')
    elif key == 'hcl':
        is_ok = check_hair_color('hcl')
    elif key == 'ecl':
        is_ok = check_eye_color('ecl')
    elif key == 'pid':
        is_ok = check_pid('pid')
    elif key == 'cid':
        is_ok = True
    return is_ok


def check_passports(input_list):
    result = []
    for i in range(0, len(input_list)):
        byr_ok = check_birth_year(input_list[i]['byr'])
        eyr_ok = check_expiration_year(input_list[i]['eyr'])
        iyr_ok = check_issue_year(input_list[i]['iyr'])
        hgt_ok = check_height(input_list[i]['hgt'])
        hcl_ok = check_hair_color(input_list[i]['hcl'])
        ecl_ok = check_eye_color(input_list[i]['ecl'])
        pid_ok = check_pid(input_list[i]['pid'])
        if byr_ok and eyr_ok and iyr_ok and ecl_ok and pid_ok and hcl_ok and hgt_ok:
            result.append(input_list[i])
    count = len(result)
    return count
