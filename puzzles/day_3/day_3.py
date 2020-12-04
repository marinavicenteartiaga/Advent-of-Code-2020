from puzzles.utils import resources

input_data = resources.get_input_list_from_file("input_day3.txt")


def get_route(right, down):
    rows = len(input_data)
    columns = len(input_data[0])
    counter = 0
    i = 0
    selected_values = []
    while i < rows:
        selected_values.append(input_data[i][counter])
        counter = (counter + right) % columns
        i += down
    n_trees = selected_values.count('#')
    return n_trees


def main():
    results = []
    down = -1
    right = -1
    while down != 0 and right != 0:
        right = int(input("Right (0 to finish): "))
        down = int(input("Down (0 to finish): "))
        if down != 0 and right != 0:
            result = get_route(right, down)
            results.append(int(result))
    final_result = 1
    for i in results:
        final_result *= i
    print(results)
    print(final_result)


main()
