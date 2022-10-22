import sys
import time
import os


def create_file() -> None:
    command = sys.argv
    directory_path = ""
    if "-d" in command:
        index = command.index("-d")
        for word in command[index + 1:]:
            if word == "-f":
                return
            directory_path += f"{word}/"
        os.makedirs(directory_path)
    if "-f" in command:
        directory_path += f"{command[-1]}"
        string_number = 1
        with open(directory_path, "a") as new_file:
            time_now = time.localtime()
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time_now)
            new_file.write(f"{time_stamp}\n")
            while True:
                new_string = input("Enter content line: ")
                if new_string == "stop":
                    new_file.write("\n")
                    return
                new_file.write(f"{string_number} {new_string}\n")
                string_number += 1


create_file()
