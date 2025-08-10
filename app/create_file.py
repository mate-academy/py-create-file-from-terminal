import datetime
import os
import sys


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(date + "\n")
        line = 1
        content = input("Enter content line: ")
        while content != "stop":
            content = input("Enter content line: ")
            file.write(f"{line} Line{line} {content} \n")
            line += 1
        file.write("\n")


def main() -> None:
    parameters = sys.argv
    index_f = None if "-f" not in parameters else parameters.index("-f")
    index_d = None if "-d" not in parameters else parameters.index("-d")
    file_name = parameters[index_f + 1]

    if index_d is not None and index_f is not None:
        if index_f < index_d:
            file_name = parameters[index_f + 1]
            directory_path = os.path.join(*parameters[index_d + 1 :])
        else:
            directory_path = os.path.join(*parameters[index_d + 1 : index_f])

        create_directory(directory_path)

        full_file_path = os.path.join(directory_path, file_name)
        create_file(full_file_path)

        print(f"Directory '{directory_path}' created")
        print(f"File '{file_name}' created")

    elif index_d is not None:
        directory_path = os.path.join(*parameters[2:])
        create_directory(directory_path)
        print(f"Directory '{directory_path}' created")

    elif index_f is not None:
        file_path = parameters[2]
        create_file(file_path)
        print(f"File '{file_name}' created")
    else:
        print("You enter incorrect command")


if __name__ == "__main__":
    main()
