from puzzles.utils import resources

with open('input_day6.txt', 'r') as file:
    input_data = []
    f = file.read().split('\n\n')
    for line in f:
        input_data.append(line.split())
#print(input_data)


def get_total_answers(data):
    result = []
    for element in range(0, len(data)):
        final_list = []
        aux = []
        if len(data[element]) > 1:
            for i in range(0, len(data[element])):
                final_list = list(set(final_list) | set(data[element][i]))
            result.append(final_list)
        else:
            for i in range(0, len(data[element])):
                one_element = data[element][i]
                for j in range(0, len(one_element)):
                    aux.append(list(one_element[j]))
                    for k in range(0, len(aux)):
                        final_list = list(set(final_list) | set(aux[k]))
            result.append(final_list)
    return result


def get_common_elements(a_list):
    final_list = []
    for i in range(0, len(a_list)):
        one_element = a_list[i]
        final_list.append(list(one_element.strip()))

    return final_list


def get_separated_answers(data):
    result = []
    for element in range(0, len(data)):
        final_list = []
        aux = []
        if len(data[element]) > 1:
            f_l = get_common_elements(data[element])
            for n in range(0, len(f_l)):
                for x in range(0, len(f_l[n])):
                    final_list = list(set(f_l[n]).intersection(*f_l))
            result.append(final_list)
        else:
            for i in range(0, len(data[element])):
                one_element = data[element][i]
                for j in range(0, len(one_element)):
                    aux.append(list(one_element[j]))
                    for k in range(0, len(aux)):
                        final_list = list(set(final_list) | set(aux[k]))
            result.append(final_list)
    return result


def count_answers(answers_list):
    result = 0
    for i in range(0, len(answers_list)):
        result = result + len(answers_list[i])
    return result


def main():
    answers_list = get_total_answers(input_data)
    common_list = get_separated_answers(input_data)

    print('The number of answers is:', count_answers(answers_list))
    print('The number of matching answers is:', count_answers(common_list))


main()
