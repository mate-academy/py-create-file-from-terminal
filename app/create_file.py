import os
import sys
import datetime


def create_file() -> None:
    if len(sys.argv) < 2:
        return
    flag = sys.argv[1]
    both_flags = sys.argv
    if "-f" in both_flags and "-d" in both_flags:
        f_index = sys.argv.index("-f")
        d_index = sys.argv.index("-d")
        if f_index > d_index:
            dir_parts = sys.argv[2:f_index]
            file_name = sys.argv[f_index + 1]
        elif f_index < d_index:
            dir_parts = sys.argv[f_index + 1:]
            file_name = sys.argv[d_index + 1]

        current_path = ""
        for part in dir_parts:
            current_path = os.path.join(current_path, part)
        os.makedirs(current_path, exist_ok=True)

        file_path = os.path.join(current_path, file_name)
        with open(file_path, "a") as new_file:
            counter = 1
            today = datetime.datetime.now()
            timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
            new_file.write("\n" + str(timestamp) + "\n")
            while True:
                text = input("Enter content line: ")
                if not text:
                    break
                if text.lower() == "stop":
                    break
                else:
                    new_file.write(str(counter) + " " + text + "\n")
                    counter += 1

    elif flag == "-d":
        current_path = ""
        for part in sys.argv[2:]:
            current_path = os.path.join(current_path, part)
        os.makedirs(current_path, exist_ok=True)

    elif flag == "-f":
        file_name = sys.argv[2]
        with open(file_name, "a") as new_file:
            counter = 1
            today = datetime.datetime.now()
            timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
            new_file.write("\n" + str(timestamp) + "\n")
            while True:
                text = input("Enter content line: ")
                if not text:
                    break
                if text.lower() == "stop":
                    break
                else:
                    new_file.write(str(counter) + " " + text + "\n")
                    counter += 1


if __name__ == "__main__":
    create_file()
