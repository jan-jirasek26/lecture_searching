from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    with open(file_name, "r") as json_file:
        dict = json.load(json_file)

    if field not in dict.keys():
        return None
    else:
        sequential_data = dict[field]
        return sequential_data

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

def linear_search(sequence, wanted_num):
    positions = []
    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i] == wanted_num:
            positions.append(i)
            count += 1
            i += 1
        else:
            i += 1

    return positions, count

def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    print(sequence)

    if sequence == None:
        return None
    else:
        wanted_number = 0
        positions, count = linear_search(sequence, wanted_number)
        print(f"Hledané číslo {wanted_number} se nachází na pozicích: {positions}, celkový počet výskytů: {count}")

if __name__ == "__main__":
    main()
