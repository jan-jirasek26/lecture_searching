from pathlib import Path
import matplotlib.pyplot as plt
import generators as gen
import json
import time

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

    start_l = time.perf_counter()

    for num in sequence:
        if num == wanted_num:
            positions.append(i)
            count += 1
            i += 1
        else:
            i += 1

    end_l = time.perf_counter()

    duration_l = end_l - start_l

    return positions, count, duration_l
"""
Sekvenční vyhledávání v neseřazeném seznamu projde všechny prvky prootže hledaná hodnota může být kdekoliv

                    Kdy nastane?            Asymptotická složitost
Nejlepší scénář         i = 0                       O(1)
Nejhorší scénář         i = None                    O(n)

"""

def binary_search(sequence, wanted_num):
    left = 0
    right = len(sequence)

    start_b = time.perf_counter()

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
    end_b = time.perf_counter()

    duration_b = end_b - start_b
    return sequence.index(wanted_num), duration_b
"""
Binárním vyhledáváním zmenšujeme počet proledávaných prvků v jednotlivých krocích: n/2, n/4...

1. Prvek se nachází v sezanamu
                    Kdy nastane?            Asymptotická složitost
Nejlepší scénář      je uprostřed                      O(1)
Nejhorší scénář      je na kraji                       O(log(n))

2. Prvek se nenachází v seznamu
                    Kdy nastane?            Asymptotická složitost
Nejlepší scénář      vždy                              O(log(n)
Nejhorší scénář      vždy                              O(log(n)

"""

def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    sequence_ord = read_data("sequential.json", "ordered_numbers")

    if sequence == None:
        return None
    else:
        wanted_number = 22
        positions, count, duration_l = linear_search(sequence, wanted_number)
        binary_search(sequence_ord, wanted_number)

if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    times_l = []
    for size in sizes:
        positions, count, duration_l = linear_search(gen.unordered_sequence(size), 50)
        times_l.append(duration_l)

    times_b = []
    for size in sizes:
        sequence = gen.ordered_sequence(size)
        index, duration_b = binary_search(sequence, sequence[5])
        times_b.append(duration_b)

    import matplotlib.pyplot as plt

    #plt.plot(sizes, times_l)
    plt.plot(sizes, times_b)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()
