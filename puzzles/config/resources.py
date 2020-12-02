def get_input_str_from_file(file):
    my_file = open(file, "r")
    values_str = ""
    for line in my_file:
        stripped_line = line.rstrip()
        values_str += stripped_line + " "
    my_file.close()
    return values_str


def str_to_list(input_string):
    result_list = list(input_string.split(" "))
    n = len(result_list)
    result_list.remove(result_list[n-1])
    return result_list


def print_input_list(input_string):
    print(str_to_list(input_string))
