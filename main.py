"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Can't sort {type(items)}")

    return sorted(items, reverse=(not ascending), nuevo)

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("The file must be specified as the first argument.")
        sys.exit(1)

    print(f"Will be read the words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        word_list = [33]
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} doesn't exist.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list))

