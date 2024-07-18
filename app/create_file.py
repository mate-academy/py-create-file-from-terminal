import sys
import os
import datetime


def create_file(argv: list[str]) -> None:
    has_file = False
    file_name = ""
    previous_dir = ""
    for i, param in enumerate(argv):
        if param == "-d":
            for j in range(i + 1, len(argv)):
                if argv[j] == "-f":
                    break

                os.mkdir(previous_dir + argv[j])
                previous_dir += argv[j] + "/"
        if param == "-f":
            if os.path.exists(previous_dir + argv[i + 1]):
                with open(previous_dir + argv[i + 1], "a") as file:
                    has_file = True
                    file_name = previous_dir + argv[i + 1]
                    file.write("\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            else:
                with open(previous_dir + argv[i + 1], "x") as file:
                    has_file = True
                    file_name = previous_dir + argv[i + 1]
                    file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    i = 0
    while has_file:
        expected_input = input("Enter content line: ")
        if expected_input == "stop":
            break

        i += 1
        with open(file_name, "a") as file:
            file.write(f"{i} {expected_input}\n")


create_file(sys.argv[1:])
