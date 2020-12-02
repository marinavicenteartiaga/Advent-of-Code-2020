from puzzles.config import resources


def find_matching_values(values):
    while values:  # not  empty
        for i in range(0, len(values)):
            main_value = int(values[i])
            number = 2020 - int(main_value)
            for x in range(i, len(values)):
                if int(values[x]) == number:
                    return print("The final result is: ", main_value * number)
                x += 1
            i += 1


def main():
    input_string = resources.get_input_str_from_file("input_day1.txt")
    values = resources.str_to_list(input_string)
    resources.print_input_list(input_string)
    find_matching_values(values)


main()
