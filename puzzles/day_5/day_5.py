from puzzles.utils import resources

input_data = resources.get_input_list_from_file("input_day5.txt")


def get_seat_id(boarding_pass):
    rows = boarding_pass[0:7]  # The first seven characters
    columns = boarding_pass[7:10]  # The last three characters
    for i in range(0, len(boarding_pass)):
        rows = rows.replace('F', '0')  # Replace F and B to make it binary
        rows = rows.replace('B', '1')
        columns = columns.replace('L', '0')
        columns = columns.replace('R', '1')
    return int(rows, 2) * 8 + int(columns, 2)  # Calculate the ID (Binary to decimal (base 2))


def get_my_seat_id(max_id, all_ids):
    for id in range(0, max_id):  # From id 0 to the maximum id
        # If the id is not the list and the seats with IDs +1 and -1 from the list too
        if id not in all_ids and (id + 1) in all_ids and (id - 1) in all_ids:
            return id


def main():
    all_ids = []

    for element in input_data:
        all_ids.append(get_seat_id(element))
    print(all_ids)
    print("The highest seat ID on a boarding pass is: ", max(all_ids))
    max_id = int(max(all_ids))
    print("My seat ID is: ", get_my_seat_id(max_id, all_ids))


main()
