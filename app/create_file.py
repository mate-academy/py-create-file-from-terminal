import os
import sys
from datetime import datetime


def main():
    args = sys.argv[1:]
    dir_parts = []
    filename = None

    d_index = None
    f_index = None
    if "-d" in args:
        d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")

    if f_index is not None:
        if f_index + 1 < len(args) and args[f_index + 1] not in ("-d", "-f"):
            filename = args[f_index + 1]
        else:
            print("Erro: Flag -f fornecido sem um nome de arquivo.")
            sys.exit(1)

    if d_index is not None:
        end_slice = len(args)
        if f_index is not None and f_index > d_index:
            end_slice = f_index
        dir_parts = args[d_index + 1:end_slice]
        if not dir_parts:
            print("Erro: Flag -d fornecido sem um caminho de diretório.")
            sys.exit(1)

    if not dir_parts and not filename:
        print(
            "Erro: Nenhum argumento fornecido. Use -d para diretório "
            "e -f para nome de arquivo."
        )
        sys.exit(1)

    target_path = "."
    if dir_parts:
        target_path = os.path.join(*dir_parts)
        os.makedirs(target_path, exist_ok=True)
        print(f"Diretório criado/assegurado: {target_path}")

    if not filename:
        return

    full_file_path = os.path.join(target_path, filename)
    print(f"Abrindo arquivo: {full_file_path}")

    with open(full_file_path, "a", encoding="utf-8") as file_obj:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_obj.write(f"\n{timestamp}\n")

        print("Enter content line (type 'stop' to finish):")
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.strip().lower() == "stop":
                break
            file_obj.write(f"{line_number} {user_input}\n")
            line_number += 1

    print(f"Conteúdo salvo com sucesso em: {full_file_path}")


if __name__ == "__main__":
    main()