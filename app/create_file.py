import argparse
import os
import datetime


def get_line_count(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return 0

    with open(filename, 'rb') as file:
        file.seek(0, os.SEEK_END)  # Перемещаем курсор в конец файла
        position = file.tell()  # Получаем общую длину файла
        line = b''

        # Читаем файл с конца, пока не найдём последнюю строку
        while position > 0:
            position -= 1
            file.seek(position)
            char = file.read(1)

            # Проверяем на конец строки
            if char == b'\n' and line:
                break
            line = char + line

        # Если файл полностью пуст, возвращаем 0 строк
        if not line.strip():
            return 0

        # Получаем номер последней строки
        try:
            last_line_number = int(line.split(b" ")[0])
        except ValueError:
            return 0

        return last_line_number


def append_content_to_file(filename: str) -> datetime:
    file_exists = os.path.exists(filename)

    # Открываем файл в режиме "дозаписи"
    with open(filename, "a") as file:
        if not file_exists:
            # Если файл ещё не существует, добавляем временную метку
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + "\n")

        # Получаем текущее количество строк
        line_number = get_line_count(filename)

        print("Write Stop to exit")
        while True:
            # Запрос строки от пользователя
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            line_number += 1
            file.write(f"{line_number} {line}\n")

    print(f"Content added success!: {filename}")


def main() -> None:
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(
        description="Добавление контента в файл"
                    " с нумерацией и временной меткой."
    )

    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Имя файла, в который будет записано содержимое."
    )

    # Парсинг аргументов
    args = parser.parse_args()

    # Вызываем основную функцию
    append_content_to_file(args.file)


if __name__ == "__main__":
    main()
