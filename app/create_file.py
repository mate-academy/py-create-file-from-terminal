from sys import argv

from os import makedirs, path

from datetime import datetime


def create_file(input_text):
    path_directory = []
    if "-d" in input_text:
        for word in range(input_text.index("-d") + 1), len(input_text):
            if input_text[word] == "-f":
                break
            path_directory.append(input_text[word])
    makedirs(path.join(**input_text))

    if "-f" in input_text:
        path_directory.append(input_text[input_text.index("-f") + 1])

        with open(path.join(**input_text), "w") as text:
            line_number = 1
            text.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            text.write("/n")
            while True:
                input_word = input("Enter content line: ")
                if input == "stop":
                    return
                text.write(f"{line_number} {input_word}")
                line_number += 1


create_file(argv)
