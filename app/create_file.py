# create_file.py

import sys
import os
from datetime import datetime


def main():
    args = sys.argv[1:]

    if not args:
        print("Uso:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    dir_path = None
    file_name = None

    # Processa os argumentos
    if "-d" in args:
        d_index = args.index("-d")
        # Coleta diretórios até achar outro flag ou fim
        dir_parts = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)
        dir_path = os.path.join(*dir_parts) if dir_parts else None

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Erro: nome do arquivo não fornecido após -f")
            sys.exit(1)

    # Cria diretório se necessário
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # Caminho final do arquivo
    if file_name:
        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name
    else:
        print("Erro: você precisa passar -f para criar arquivo")
        sys.exit(1)

    # Captura conteúdo do usuário
    lines = []
    counter = 1
    print("Digite linhas de conteúdo (digite 'stop' para terminar):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    if not lines:
        print("Nenhuma linha adicionada, nada foi escrito no arquivo.")
        sys.exit(0)

    # Cria bloco de conteúdo com timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block
