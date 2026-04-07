import datetime
import os
import sys


def check_for_d(input_data: list) -> None:
    if "-d" in input_data:
        new_folder = input_data[input_data.index("-d")
                                + 1:input_data.index("-f")]
        path = os.path.join(*new_folder)
        os.makedirs(path, exist_ok=True)
        create_file(os.path.join(*new_folder + [input_data[-1]]))
    else:
        check_for_f(input_data)


def check_for_f(input_data: list) -> None:
    if not input_data:
        print("Введіть коректну назву файлу")
        return
    if "-f" not in input_data:
        print("Введіть правильну команду")
        return
    path = ("").join(input_data[-1])
    create_file(path)


def create_file(path: str) -> None:
    date_log = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if os.path.exists(path):
        date_log = "\n\n" + date_log
    with open(path, "a") as file:
        file.write(date_log)
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"\n{new_line}")


check_for_d(sys.argv)
