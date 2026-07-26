import os
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Ошибка: Недостаточно аргументов.")
    sys.exit(1)

operand = sys.argv[1:]
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

if operand[0] == "-f":
    if len(operand) < 2:
        print("Ошибка: Недостающее имя файла для опции '-f'.")
        sys.exit(1)

    file_name = operand[1]
    try:
        with open(file_name, "a", encoding="utf-8") as source_file:
            source_file.write(formatted_date + "\n")
            index = 1
            while True:
                message = input("Enter content line: ")

                if message.lower() == "stop":
                    break

                source_file.write(f"{index} {message}\n")
                index += 1

            source_file.write("\n")
        print(f"Контент успешно записан в '{file_name}'.")
    except Exception as e:
        print(f"Ошибка: "
              f"Невозможно записать в файл '{file_name}'. Причина: {e}")

elif operand[0] == "-d":
    directories = []
    for i in range(1, len(operand)):
        if operand[i] == "-f":
            break
        directories.append(operand[i])

    formatted_path = os.path.join(*directories)
    try:
        os.makedirs(formatted_path, exist_ok=True)
        print(f"Директории успешно созданы: {formatted_path}")
        if "-f" in operand:
            file_index = operand.index("-f") + 1
            if file_index < len(operand):
                file_name = operand[file_index]
                file_path = os.path.join(formatted_path, file_name)

                with open(file_path, "a", encoding="utf-8") as source_file:
                    source_file.write(formatted_date + "\n")
                    index = 1
                    while True:
                        message = input("Enter content line: ")

                        if message.lower() == "stop":
                            break

                        source_file.write(f"{index} {message}\n")
                        index += 1

                    source_file.write("\n")
                print(f"Файл '{file_name}' успешно "
                      f"создан в '{formatted_path}'.")
    except Exception as e:
        print(f"Невозможно создать директории или файл. Причина: {e}")
else:
    print("Неверная опция. Используйте '-f' "
          "для работы с файлами или '-d' для создания директорий.")
