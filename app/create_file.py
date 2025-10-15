#!/usr/bin/env python3
import sys
import os
from datetime import datetime


def get_content():
    """Recebe linhas de conteúdo do usuário até 'stop'."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_file(file_path, lines):
    """Escreve linhas no arquivo com timestamp e numeração."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_to_write = f"{timestamp}\n"
    for i, line in enumerate(lines, start=1):
        content_to_write += f"{i} {line}\n"
    # Se o arquivo existir, adiciona separador de linha
    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n" + content_to_write)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content_to_write)
    print(f"Content written to {file_path}")


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file.txt]")
        sys.exit(1)

    dirs = []
    file_name = None

    # Parsing simples dos argumentos
    if "-d" in args:
        d_index = args.index("-d")
        # tudo até o próximo flag ou final
        next_flags = [i for i, a in enumerate(args) if a in ("-f",) and i > d_index]
        end_index = next_flags[0] if next_flags else len(args)
        dirs = args[d_index + 1:end_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            print("Error: Missing file name after -f")
            sys.exit(1)
        file_name = args[f_index + 1]

    # Cria diretórios, se houver
    dir_path = os.path.join(*dirs) if dirs else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # Determina caminho final do arquivo
    if file_name:
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name
        lines = get_content()
        write_file(file_path, lines)
    else:
        print("No file specified. Only directories were created.")


if __name__ == "__main__":
    main()

