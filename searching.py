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
    for num in sequence:
        if num == wanted_num:
            positions.append(i)
            count += 1
            i += 1
        else:
            i += 1

    return positions, count
"""
Sekvenční vyhledávání v neseřazeném seznamu projde všechny prvky prootže hledaná hodnota může být kdekoliv

                    Kdy nastane?            Asymptotická složitost
Nejlepší scénář         i = 0                       O(1)
Nejhorší scénář         i = None                    O(n)

"""

def binary_search(sequence, wanted_num):
    left = 0
    right = len(sequence)
    while True:
        if wanted_num not in sequence:
            return None

        middle = int((left + right) / 2)
        x = sequence[middle]

        if sequence[middle] == wanted_num:
            break
        elif sequence[middle] < wanted_num:
            left = middle
            continue
        elif sequence[middle] > wanted_num:
            right = middle
            continue

    return sequence.index(wanted_num)

def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    sequence_ord = read_data("sequential.json", "ordered_numbers")
    #print(sequence)
    print(sequence_ord)

    if sequence == None:
        return None
    else:
        wanted_number = 22
        #positions, count = linear_search(sequence, wanted_number)
        #print(f"Hledané číslo {wanted_number} se nachází na pozicích: {positions}, celkový počet výskytů: {count}")
        print(binary_search(sequence_ord, wanted_number))
if __name__ == "__main__":
    main()
