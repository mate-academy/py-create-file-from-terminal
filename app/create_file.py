import argparse
import os
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

    args = parser.parse_args()

    dir_path = None
    file_path = None

    # 1) -d foi passado → monta o caminho do diretório
    if args.d:
        dir_path = os.path.join(*args.d)
        os.makedirs(dir_path, exist_ok=True)

    # 2) -f foi passado → define onde o arquivo será criado
    if args.f:
        file_name = args.f

        # -f sozinho → arquivo no diretório atual
        if dir_path is None:
            file_path = file_name
        # -d e -f juntos → arquivo dentro do diretório
        else:
            file_path = os.path.join(dir_path, file_name)

    # 3) Se não há arquivo para escrever, encerra
    if file_path is None:
        return

    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 4) Escrita controlada no arquivo
    file_exists_and_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0

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
