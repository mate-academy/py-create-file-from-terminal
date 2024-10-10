import sys
import os
import datetime


def main() -> None:
    def create_path_and_file_name(arguments: list) -> list:
        file_name = ""
        directory = []
        flag = True
        for value in arguments:
            if value == "-f":
                flag = False
            if flag and value != "-d":
                directory.append(value)
            elif value not in ("-d", "-f"):
                file_name = value
        return [directory, file_name]

    def create_dir(directory: list) -> None:
        for direc in directory:
            if not os.path.exists(direc):
                os.mkdir(direc)
            os.chdir(direc)

    def write_information_into_file(file_name: str) -> None:
        with open(file_name, "w") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d "
                                                        "%H:%M:%S") + "\n")
            while True:
                content_line = input("Enter content line: ")
                if content_line == "stop":
                    break
                file.write(content_line + "\n")

    input_arguments = sys.argv
    input_arguments.pop(0)
    os.chdir("app")
    path = create_path_and_file_name(input_arguments)
    if "-d" not in input_arguments:
        write_information_into_file(path[1])
    else:
        create_dir(path[0])
        write_information_into_file(path[1])


if __name__ == "__main__":
    main()
