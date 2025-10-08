import sys
import os
from datetime import datetime
from typing import LiteralString


class MissingArgumentError(Exception):

    def __init__(self,
                 flag: str = "",
                 message: str = "A required argument is missing."
                 ) -> None:
        self.message = message
        self.flag = flag
        super().__init__(self.message)

    def __str__(self) -> str:
        message_map = {
            "-d": "A directory name is required.",
            "-f": "A file name is required."
        }
        if self.flag in message_map:
            return f"{self.message} \n\n{message_map[self.flag]}"
        return self.message


class MissingFlagError(MissingArgumentError):

    def __init__(
            self,
            message: str = "A required flag is missing."
    ) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return (
            f"{self.message} \n\n"
            f"You must provide at least a -d flag "
            f"and a directory name to create a directory. \n"
            f"Usage: python {sys.argv[0]} -d <directory_name> \n"
            f"Usage for recursive directories: "
            f"python {sys.argv[0]} "
            f"-d <directory_name> <directory_name> \n\n"
            f"You must provide at least a -f flag "
            f"and a file name to create a file. \n"
            f"Usage: python {sys.argv[0]} -f <file_name> \n\n"
            f"Usage for recursive files: "
            f"python {sys.argv[0]} -d <directory_name> -f <file_name> \n"
        )


def make_path(parts: list) -> LiteralString | str | bytes:

    if len(parts) > 0:
        return os.path.join(*parts)
    else:
        return ""


def create_directories(directory_path: LiteralString | str | bytes) -> bool:
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError:
        return False
    else:
        return True


def write_to_file(filename: LiteralString | str | bytes) -> None:
    file_exists = os.path.exists(filename)

    with open(filename, "a") as file:

        input_counter = 1

        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                break

            if input_counter == 1:

                if file_exists:
                    file.write("\n")

                date_format = "%Y-%m-%d %H:%M:%S"

                file.write(f"{datetime.now().strftime(date_format)}\n")

            file.write(f"{input_counter} {user_input}\n")

            input_counter += 1


def process_arguments() -> None:
    if len(sys.argv) < 2:
        raise MissingFlagError()
    else:
        if sys.argv[1] == "-d":

            if len(sys.argv) < 3:
                raise MissingArgumentError("-d")

            if "-f" in sys.argv:
                dir_path = make_path(sys.argv[2:sys.argv.index("-f")])
                if create_directories(dir_path):
                    filename = sys.argv[sys.argv.index("-f") + 1]
                    file_path = make_path([dir_path, filename])
                    write_to_file(file_path)
            else:
                create_directories(make_path(sys.argv[2:]))
        elif sys.argv[1] == "-f":
            if len(sys.argv) < 3:
                raise MissingArgumentError("-f")

            write_to_file(make_path([sys.argv[2]]))


# Hauptausführung des Skripts
if __name__ == "__main__":
    try:
        process_arguments()

    except MissingArgumentError as e:
        print(f"Error: {e}")
        sys.exit(2)
