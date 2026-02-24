import os
import sys
from datetime import datetime

entered_data = sys.argv[1:]  # пропускаємо ім’я скрипта
directory_path = "."
file_name = None

# Ручний парсинг аргументів
i = 0
while i < len(entered_data):
    if entered_data[i] == "-d":
        i += 1
        path_parts = []
        while i < len(entered_data) and not entered_data[i].startswith("-"):
            path_parts.append(entered_data[i])
            i += 1
        if not path_parts:
            print("Error: Missing directory path after -d flag.")
            sys.exit(1)
        directory_path = os.path.join(*path_parts)
        os.makedirs(directory_path, exist_ok=True)
    elif entered_data[i] == "-f":
        i += 1
        if i >= len(entered_data) or entered_data[i].startswith("-"):
            print("Error: Missing file name after -f flag.")
            sys.exit(1)
        file_name = entered_data[i]
        i += 1
    else:
        print(f"Unknown argument: {entered_data[i]}")
        sys.exit(1)

# Створення файлу (якщо вказано)
if file_name:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "a") as file:
        file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1
else:
    print("No -f flag provided. Only directory was created.")
