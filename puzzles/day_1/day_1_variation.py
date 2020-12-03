from puzzles.utils import resources


def find_matching_values(values):
    while values:  # not  empty
        for i in range(0, len(values)):
            first_value = int(values[i])
            value_2 = 2020 - int(first_value)
            for x in range(i, len(values)):
                if int(values[x]) < value_2:
                    second_value = int(values[x])
                    value_3 = value_2 - second_value
                    for j in range(i, len(values)):
                        if int(values[j]) == value_3:
                            return print("The final result is: ", first_value * second_value * value_3)
                        j += 1
                x += 1
            i += 1


def main():
    input_string = resources.get_input_str_from_file("input_day1.txt")
    values = resources.str_to_list(input_string)
    resources.print_input_list(input_string)
    find_matching_values(values)


main()
