import os
import sys
import datetime


def create_directory(dir_path: str) -> None:
    """Create a directory if it doesn't already exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory '{dir_path}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir_path}': {e}")


def create_file(file_path: str) -> None:
    """Create or append content to a file with timestamp and line numbering."""
    try:
        print(f"Attempting to create file at: {file_path}")  # Debugging line

        # Проверка, существует ли файл
        if os.path.isfile(file_path):
            overwrite = input(f"File '{file_path}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() != "y":
                print("Operation aborted.")
                return

        # Создание файла
        with open(file_path, "w", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")

            line_number = 1
            while True:
                line = input(f"Enter content line ({line_number}): ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1

        print(f"Content written to '{file_path}' successfully.")  # Debugging line

    except Exception as e:
        print(f"Error creating or writing to file '{file_path}': {e}")


def main() -> None:
    """Main function to handle command-line arguments and create files or directories."""
    if len(sys.argv) < 2:
        print("Usage: python create_file.py -d <dir_path> -f <file_name>")
        return

    directory = None
    file_name = None

    # Парсим аргументы командной строки
    args = sys.argv[1:]
    if "-d" in args:
        dir_index = args.index("-d") + 1
        directory = os.path.join(*args[dir_index:])
        args = args[:args.index("-d")]

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    if directory:
        create_directory(directory)

    if file_name:
        # Путь к файлу
        if directory:
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
