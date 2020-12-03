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
