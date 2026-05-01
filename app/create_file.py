from sys import argv
from os import makedirs, path
from datetime import datetime


def main() -> None:

    if len(argv) <= 2 :
        print("Usage: -f for create file or -d for create directory")
        exit(0)

    filename = ""
    directory = []
    stop = False
    content = []
    line_number = 1

    del argv[0]

    for index in range(len(argv)):
        if argv[index].strip() == "-f":
            try:
                filename = argv[index + 1].strip().lower()
                del argv[index: index + 2]
                break
            except IndexError:
                print("Error: після -f має бути вказано filename")
                exit(1)

    for index in range(len(argv)):
        if argv[index].strip() == "-d":
            if index == len(argv) - 1:
                print("Error: після -d має бути вказано dirname")
                exit(1)
            directory = [name.strip() for name in argv[index + 1:]]

    if directory != []:
        makedirs(path.join(*directory), exist_ok=True)

    if filename == "":
        exit(0)

    while not stop:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            stop = True
        else:
            content.append(f"{line_number} {line}\n")
            line_number += 1
    content.append("\n")

    with open(path.join(*directory, filename), "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in content:
            f.write(line)


if __name__ == "__main__":
    main()
