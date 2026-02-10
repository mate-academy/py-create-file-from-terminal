import argparse
import os
from datetime import datetime


def create_file() -> None:
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parser = argparse.ArgumentParser(description="Cria arquivo "
                                                 "a partir do diretório "
                                                 "e nome")
    parser.add_argument("-d", nargs="+", help="Diretórios "
                                              "que formam o caminho")
    parser.add_argument("-f", help="Nome do arquivo a ser criado")
    args = parser.parse_args()

    file_name = args.f
    dir_path = os.path.join(*args.d)
    file_path = os.path.join(dir_path, file_name)

    if not os.path.exists(file_path):
        os.makedirs(dir_path)

    with open(file_path, "a") as f:
        f.write(f"{timestamp_str}\n")
        line_counter = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            f.write(f"{line_counter} {user_input}\n")
            line_counter += 1


if __name__ == "__main__":
    create_file()
