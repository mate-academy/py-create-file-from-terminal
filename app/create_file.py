import datetime
import os
import sys


def create_dirs(input_data: list) -> None:

    if "-d" in input_data and "-f" in input_data:
        new_folder = input_data[input_data.index("-d")
                                + 1:input_data.index("-f")]
        path = os.path.join(*new_folder)
        os.makedirs(path, exist_ok=True)
        create_file(os.path.join(*new_folder + [input_data[-1]]))
        return

    if "-d" in input_data and "-f" not in input_data:
        new_folder = input_data[input_data.index("-d") + 1:]
        path = os.path.join(*new_folder)
        os.makedirs(path, exist_ok=True)
        return
    else:
        path = input_data[-1]
        create_file(path)


def create_file(path: str) -> None:
    date_log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(path):
        date_log = "\n\n" + date_log
    with open(path, "a") as file:
        file.write(date_log)
        index = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"\n{index} {new_line}")
            index += 1


def validate_for_correct_data(input_data: list) -> None:
    if "-d" not in input_data and "-f" not in input_data:
        print("No -d or -f flags provided.")
        return
    index_d = input_data.index("-d") + 1 if "-d" in input_data else None
    index_f = input_data.index("-f") + 1 if "-f" in input_data else None
    if ("-d" in input_data and "-f" not in input_data
            and len(input_data[index_d:]) == 0):
        print("No name for path of dirs")
        return
    if "-f" in input_data and "-d" not in input_data:
        if len(input_data[index_f:]) == 0 or len(input_data[index_f:]) > 1:
            print("No name for path of files")
            return
        if "." not in input_data[index_f:][0]:
            print("Input correct name of files")
            return
        create_dirs(input_data)
    else:
        create_dirs(input_data)


if __name__ == "__main__":
    validate_for_correct_data(sys.argv[1:])
