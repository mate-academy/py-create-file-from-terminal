import argparse
import datetime
import os


def main() -> None:
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

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="-d for create directory, -f for create file")
    parser.add_argument("-d", "--dir", nargs="+",
                        help="-d for create directory, -f for create file")
    command = parser.parse_args()
    os.chdir("app")
    if not command.dir:
        write_information_into_file(command.file)
    else:
        create_dir(command.dir)
        write_information_into_file(command.file)


if __name__ == "__main__":
    main()
