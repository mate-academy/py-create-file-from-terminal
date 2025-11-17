import os
import sys


def create_file(dirs: list[str], filename: str) -> None:
    # Створюємо шлях директорій
    if dirs:
        dir_path = os.path.join(*dirs)  # dir1/dir2
        os.makedirs(dir_path, exist_ok=True)
        full_path = os.path.join(dir_path, filename)
    else:
        full_path = filename

    # Визначаємо counter за кількістю рядків, якщо файл існує
    counter = 1

    print(f"Writing to: {full_path}")

    # Основний цикл
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break

        with open(full_path, "a") as f:  # "a" — append
            f.write(f"{counter} {content}\n")

        counter += 1


if __name__ == "__main__":
    args = sys.argv[1:]  # відкидаємо ім'я скрипта

    dirs = []
    files = []

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # збираємо всі директорії до наступної опції
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            # збираємо всі файли до наступної опції
            while i < len(args) and not args[i].startswith("-"):
                files.append(args[i])
                i += 1
        else:
            # якщо щось невідоме, пропускаємо
            i += 1

    print("Directories:", dirs)
    print("Files:", files[0])
    create_file(dirs, files[0])
