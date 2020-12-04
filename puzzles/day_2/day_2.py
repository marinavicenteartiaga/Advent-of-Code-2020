from puzzles.utils import resources

input_info = [[1, 3, "a", "abcde"], [1, 3, "b", "cdefg"], [2, 9, "c", "ccccccccc"]]

print(input_info)


def get_correct_passwords(input_info):
    correct_passwords = []
    cont = 0

    for i in range(0, len(input_info)):
        min = input_info[i][0]
        max = input_info[i][1]
        char = input_info[i][2]
        password = input_info[i][3]
        for j in range(0, len(password)):
            if password[j] == char:
                cont += 1
            j += 1
        if int(max) >= cont >= int(min):
            correct_passwords.append([min, max, char, password])
        cont = 0
        i += 1
    return correct_passwords


def main():
    input_list = resources.get_input_list_from_file_not_optimized("input_day2.txt")
    print(input_list)
    value_list = resources.get_data_from_input_list_format_day2(input_list)
    result = get_correct_passwords(value_list)

    for i in range(0, len(result)):
        print(result[i][0], "-", result[i][1], " ", result[i][2], ": ", result[i][3])
    print("The number of valid passwords is: ", len(result))


main()
