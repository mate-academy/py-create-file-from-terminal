import sys
from datetime import datetime
from pathlib import Path


def main() -> None:
    args = sys.argv[1:]

    # 1. Розбір аргументів
    dirs = []
    filename = ""
    current_flag = ""

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        else:
            if current_flag == "-d":
                dirs.append(arg)
            elif current_flag == "-f":
                filename = arg
                current_flag = ""

    # 2. Створення папок (мають створюватися завжди, навіть без -f)
    full_path = Path(".")
    if dirs:
        full_path = Path(*dirs)
        full_path.mkdir(parents=True, exist_ok=True)

    # 3. Робота з файлом
    if filename:
        full_filepath = full_path / filename
        lines = []

        while True:
            # ТЕСТ ОЧІКУЄ САМЕ ТАКИЙ ПРОМТ
            user_input = input("Enter content line: ")
            if user_input == "stop":  # ТІЛЬКИ ТОЧНЕ "stop"
                break
            lines.append(user_input)

        # Якщо ввели хоча б щось (або як вимагає тест - запис блоку)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = current_time + "\n"
        for index, text in enumerate(lines, start=1):
            content += f"{index} {text}\n"

        # Перевірка наявності контенту для пустих рядків
        file_exists = full_filepath.exists() and full_filepath.stat().st_size > 0

        with open(full_filepath, "a", encoding="utf-8") as file_object:
            if file_exists:
                file_object.write("\n")
            file_object.write(content)


# Щоб тести точно могли запустити функцію
if __name__ == "__main__":
    main()
