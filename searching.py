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


def pattern_search(sequence, pattern):
    indexes = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            indexes.append(i + int(0.5 * len(pattern)))
        else:
            continue
    result = set(indexes)
    return result


def main():
    number = 0
    list_of_numbers = read_data("sequential.json", "unordered_numbers")
    print(linear_search(list_of_numbers, number))
    sequence = read_data("sequential.json", "dna_sequence")
    pattern = "ATA"
    print(pattern_search(sequence, pattern))


if __name__ == '__main__':
    main()
