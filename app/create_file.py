import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(directory_path: str) -> None:
    """Создает директорию, если она не существует."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Директория создана: {directory_path}")
    else:
        print(f"Директория уже существует: {directory_path}")


def create_file(file_path: str) -> None:
    """Создает файл и добавляет в него контент."""
    content_lines: List[str] = []
    print("Введите содержимое файла. Для завершения введите 'stop':")
    while True:
        line: str = input("Введите строку содержимого: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Получаем текущее время для временной метки
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Открываем файл для добавления контента
    with open(file_path, "a", encoding="utf-8") as file:
        # Добавляем временную метку
        file.write(f"{timestamp}\n")
        # Добавляем строки контента с нумерацией
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")
        # Добавляем пустую строку для разделения блоков контента
        file.write("\n")

    print(f"Файл создан/обновлен: {file_path}")


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Использование: python create_file.py "
            "[-d dir1 dir2 ...] [-f filename]"
        )
        sys.exit(1)

    directory_path: Optional[str] = None
    file_name: Optional[str] = None

    # Обрабатываем аргументы командной строки
    i: int = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            # Собираем все аргументы после -d как части пути
            directory_parts: List[str] = []
            i += 1
            while i < len(sys.argv) and sys.argv[i] != "-f":
                directory_parts.append(sys.argv[i])
                i += 1
            directory_path = os.path.join(*directory_parts)
        elif sys.argv[i] == "-f":
            # Следующий аргумент - имя файла
            i += 1
            if i < len(sys.argv):
                file_name = sys.argv[i]
                i += 1
        else:
            i += 1

    # Создаем директорию, если указан путь
    if directory_path:
        create_directory(directory_path)

    # Создаем файл, если указано имя файла
    if file_name:
        file_path: str = (
            os.path.join(directory_path, file_name)
            if directory_path else file_name
        )
        create_file(file_path)
    else:
        print("Имя файла не указано.")


if __name__ == "__main__":
    main()
