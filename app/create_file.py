import argparse
import os
import sys
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser(
        description="Cria diretórios e/ou arquivos a partir de flags"
    )
    parser.add_argument(
        "-d",
        nargs="+",
        help="Diretórios que formam o caminho"
    )
    parser.add_argument(
        "-f",
        help="Nome do arquivo a ser criado"
    )

    # Passagem explícita de sys.argv (exigência do enunciado)
    args = parser.parse_args(sys.argv[1:])

    dir_path = None
    file_path = None

    if args.d:
        dir_path = os.path.join(*args.d)
        os.makedirs(dir_path, exist_ok=True)

    if args.f:
        file_name = args.f
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    if file_path is None:
        return

    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Linha longa dividida em duas partes
    file_exists_and_not_empty = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as f:
        if file_exists_and_not_empty:
            f.write("\n")

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
