from puzzles.utils import resources

input_info = [[1, 3, "a", "abcde"], [1, 3, "b", "cdefg"], [2, 9, "c", "ccccccccc"]]

print(input_info)


def get_correct_passwords(input_info):
    correct_passwords = []
    for i in range(0, len(input_info)):
        min = input_info[i][0]
        max = input_info[i][1]
        char = input_info[i][2]
        password = input_info[i][3]
        first_a = False
        second_a = False
        first_b = False
        second_b = False
        for j in range(0, len(password)):
            if j+1 == int(min):
                if password[j] == char:
                    first_a = True
                elif password[j] != char:
                    first_b = True
            if j+1 == int(max):
                if password[j] != char:
                    second_a = True
                elif password[j] == char:
                    second_b = True

        if (first_a is True and second_a is True) or (first_b is True and second_b is True):
            correct_passwords.append([min, max, char, password])
        i += 1
    return correct_passwords


def main():
    input_list = resources.get_input_list_from_file("input_day2.txt")
    print(input_list)
    value_list = resources.get_data_from_input_list_format_day2(input_list)
    result = get_correct_passwords(value_list)

    for i in range(0, len(result)):
        print(result[i][0], "-", result[i][1], " ", result[i][2], ": ", result[i][3])
    print("The number of valid passwords is: ", len(result))


main()
