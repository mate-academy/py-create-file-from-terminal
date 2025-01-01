import argparse
import os
import datetime


def append_content_to_file(filename: str) -> datetime:
    file_exists = os.path.exists(filename)

    with open(filename, 'a') as file:
        if not file_exists:

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(timestamp + '\n')

        line_number = sum(1 for _ in open(filename, 'r')) if file_exists else 0

        print(
            "Введите строки содержимого для файла."
            " Введите stop, чтобы завершить."
        )

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            line_number += 1
            file.write(f"{line_number} {line}\n")

    print(f"Контент успешно добавлен в файл: {filename}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Добавление контента в файл с "
                    "нумерацией и временной меткой."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Имя файла, в который будет записано содержимое."
    )

    args = parser.parse_args()

    append_content_to_file(args.file)


if __name__ == "__main__":
    main()
