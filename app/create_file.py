import sys
import os
from datetime import datetime

def create_path(directories: list) -> str:
    """Створює шлях до директорії з переданих частин."""
    path = os.path.join(*directories)
    return path

if "-d" in sys.argv:
    # Перевіряємо, чи вказано директорії після -d
    if len(sys.argv) < 3:
        print("Error: No directories provided after '-d'")
        sys.exit(1)
    os.makedirs(create_path(sys.argv[2:]), exist_ok=True)
    print(f"Directory {create_path(sys.argv[2:])} created.")

if "-f" in sys.argv:
    # Перевіряємо, чи передано ім'я файлу після -f
    if len(sys.argv) < 3:
        print("Error: No filename provided after '-f'")
        sys.exit(1)

    filename = sys.argv[2]
    with open(filename, "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        i = 1
        while True:
            x = input("Enter content line: ")
            if x == "stop":
                break
            file.write(f"{i} {x}\n")
            i += 1
    print(f"File '{filename}' created with content.")