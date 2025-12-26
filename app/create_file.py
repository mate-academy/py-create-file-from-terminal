import sys
import os
import datetime


def create_directory(path: str) -> None:
    """Створює каталог за вказаним шляхом, якщо він ще не існує."""
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    """Створює файл, запитуючи користувача про введення вмісту."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    append_mode = os.path.exists(file_path)

    with open(file_path, "a" if append_mode else "w") as file:
        if append_mode:
            file.write("\n\n")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    dir_path = None
    if "-d" in args:
        index = args.index("-d")
        dir_args = args[index + 1:]
        if "-f" in dir_args:
            file_index = dir_args.index("-f")
            dir_args = dir_args[:file_index]
        if not dir_args:
            print("Помилка: необхідно вказати шлях до каталогу після -d")
            return
        dir_path = os.path.join(*dir_args)
        create_directory(str(dir_path))

    if "-f" in args:
        index = args.index("-f")
        if index + 1 < len(args):
            file_name = args[index + 1]
            file_path = os.path.join(str(dir_path),
                                     file_name) if dir_path else file_name
            create_file(file_path)
        else:
            print("Помилка: не вказано ім'я файлу для -f")
    else:
        print("Помилка: необхідно передати прапорець "
              "-d для каталогу або -f для файлу.")


if __name__ == "__main__":
    main()
