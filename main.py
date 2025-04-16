"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=not ascending)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Se debe indicar el fichero como primer argumento")
        sys.exit(1)

    filename = sys.argv[1]
    ascending = True  # Por defecto orden ascendente

    # Si hay un segundo argumento, definimos el orden
    if len(sys.argv) >= 3:
        order = sys.argv[2].lower()
        if order == "desc":
            ascending = False
        elif order != "asc":
            print("Orden no reconocido. Usando orden ascendente por defecto.")

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word = line.strip()
                if word:  # Evita agregar líneas vacías
                    word_list.append(word)
    else:
        print(f"El fichero {filename} no existe. Se usará una lista por defecto.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    sorted_words = sort_list(word_list, ascending=ascending)
    print("Palabras ordenadas:")
    for word in sorted_words:
        print(word)
