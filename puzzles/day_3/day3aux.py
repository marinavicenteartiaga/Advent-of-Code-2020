from puzzles.utils import resources

input_list = resources.get_input_list_from_file_not_optimized("input_day3.txt")


def check_end_of_column():
    return True


def check_end_of_row():
    return True


def tree_or_square(input_list, position):
    symbol = ""
    row = []
    if chr(input_list[position]) == ".":
        symbol = "O"
    elif chr(input_list[position]) == "#":
        symbol = "X"
    return symbol


def get_map(input_list):
    list_of_list = []
    n_x = 0
    for i in range(0, len(input_list)):
        list_of_list.append(list(input_list[i].strip()))
        pos = i * 3
        if pos <= len(input_list[i]):
            if list_of_list[i][pos] == '.':
                list_of_list[i][pos] = 'O'
            elif list_of_list[i][pos] == '#':
                list_of_list[i][pos] = 'X'
                n_x += 1
        else:
            pos = pos - len(input_list[i])
            if pos <= len(input_list[i]):
                if list_of_list[i][pos] == '.':
                    list_of_list[i][pos] = 'O'
                elif list_of_list[i][pos] == '#':
                    list_of_list[i][pos] = 'X'
                    n_x += 1
    print(n_x)
    return n_x


def main():
    input_list = resources.get_input_list_from_file_not_optimized("input_day3.txt")
    result = get_map(input_list)
    #for i in range(0, len(input_list)):
        #print(result[i])
    result


main()
