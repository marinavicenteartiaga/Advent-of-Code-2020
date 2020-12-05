def get_input_str_from_file(file):
    my_file = open(file, "r")
    values_str = ""
    for line in my_file:
        stripped_line = line.rstrip()
        values_str += stripped_line + " "
    my_file.close()
    return values_str

def get_input_list_from_file(file):
    my_file = open(file, "r")
    values_str = []
    for line in my_file:
        stripped_line = line.rstrip()
        values_str.append(stripped_line)
    my_file.close()
    return values_str

def get_input_list_from_file(file):
    with open(file, 'r') as file:
        values = [line.strip() for line in file]
    return values


def get_data_from_input_list_format_day2(input_list):
    values = []
    value_list = []
    for i in range(0, len(input_list)):
        element = input_list[i]
        values.append(element.split(" ", 2))
        min_max = values[i][0].split("-", 1)
        minimum = min_max[0]
        maximum = min_max[1]
        char = values[i][1][0]
        password = values[i][2]
        value_list.append([minimum, maximum, char, password])
    return value_list


def str_to_list(input_string):
    result_list = list(input_string.split(" "))
    n = len(result_list)
    result_list.remove(result_list[n-1])
    return result_list


def print_input_list(input_string):
    print(str_to_list(input_string))


def input_text_to_list_of_dictionaries(passports):
    all_keys_values = []
    for passport in range(0, len(passports)):
        keys = []
        values = []
        key_value = []
        is_ok = True
        for element in range(0, len(passports[passport])):
            key = ''
            value = ''
            for i in range(0, len(passports[passport][element])):
                key = key + passports[passport][element][i]
                if i == 2:
                    keys.append(key)
                    key = ''
                if i > 3:
                    value = value + passports[passport][element][i]
            values.append(value)
        key_value.append(keys)
        key_value.append(values)
        all_keys_values.append(key_value)

    ld = []
    for i in range(0, len(all_keys_values)):
        d = dict(zip(all_keys_values[i][0], all_keys_values[i][1]))
        ld.append(d)

    return ld

