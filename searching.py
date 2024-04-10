import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]


def linear_search(sequence, number):
    keys = ["positions", "count"]
    list_of_indexes = []
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == number:
            list_of_indexes.append(i)
            count += 1
        else:
            continue
    result = [list_of_indexes, count]
    return dict(zip(keys, result))


def main():
    number = 0
    print(linear_search(read_data("sequential.json", "unordered_numbers"), number))


if __name__ == '__main__':
    main()
