import argparse
import os
import datetime


def append_content_to_file(filename):
    """
    Добавляет содержимое в существующий файл или создаёт новый файл.
    Первой строкой добавляется текущая временная метка, затем строки нумеруются.
    Запись прекращается при вводе 'stop'.
    """
    # Проверка, существует ли файл
    file_exists = os.path.exists(filename)

    # Открываем файл в режиме "дозаписи"
    with open(filename, 'a') as file:
        if not file_exists:
            # Если файл ещё не существует, добавляем временную метку
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(timestamp + '\n')

        # Счётчик строк (для нумерации контента)
        line_number = sum(1 for _ in open(filename, 'r')) if file_exists else 0

        print("Введите строки содержимого для файла. Введите 'stop', чтобы завершить.")
        while True:
            # Запрос строки от пользователя
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            line_number += 1
            file.write(f"{line_number} {line}\n")

    print(f"Контент успешно добавлен в файл: {filename}")


def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description="Добавление контента в файл с нумерацией и временной меткой.")
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
