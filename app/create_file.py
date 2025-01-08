import os
import sys
from datetime import datetime


class FileCreatorError(Exception):
    pass


def create_directories(base_path: str, dirs: list) -> str:
    if not dirs:
        raise FileCreatorError("No directories specified after '-d'.")

    path = os.path.join(base_path, *dirs)
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise FileCreatorError(f"Error creating directories: {e}")

    return path


def write_to_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            print("Enter content line by line. Type 'stop' to finish.")
            line_count = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    file.write("\n")
                    break
                if line.strip():
                    file.write(f"{line_count} {line}\n")
                    line_count += 1
    except Exception as e:
        raise FileCreatorError(f"Error writing to file: {e}")


def parse_arguments() -> tuple[list[str], str]:
    if "-f" not in sys.argv:
        raise FileCreatorError(
            "Filename not specified. Use '-f [filename]' to specify a file."
        )

    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1] if f_index + 1 < len(sys.argv) else None
    if not file_name:
        raise FileCreatorError("Filename is missing after '-f'.")

    dirs = []
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dirs = sys.argv[d_index + 1:f_index] if d_index + 1 < f_index else []

    return dirs, file_name


def main() -> None:
    try:
        dirs, file_name = parse_arguments()
        base_path = os.getcwd()
        if dirs:
            base_path = create_directories(base_path, dirs)
        file_path = os.path.join(base_path, file_name)
        print(f"Writing to file: {file_path}")
        write_to_file(file_path)

    except FileCreatorError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
