#!/usr/bin/env python3
import sys
import os
from datetime import datetime


def get_content():
    """Recebe linhas de conteúdo do usuário até 'stop'."""
    lines = []
    while True:
        line = input("Enter content line:")  # prompt exato
        if line == "stop":  # case-sensitive
            break
        lines.append(line)
    return lines


def write_file(file_path, lines):
    """Escreve linhas no arquivo com timestamp e numeração, garantindo exatamente uma linha em branco entre blocos."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_to_write = f"{timestamp}\n"
    for line_number, line_text in enumerate(lines, start=1):
        content_to_write += f"{line_number} {line_text}\n"

    if os.path.exists(file_path):
        # Lê o conteúdo existente e normaliza as quebras de linha
        with open(file_path, "r", encoding="utf-8") as existing_file:
            existing_content = existing_file.read()
        # Remove múltiplas quebras no final
        stripped_content = existing_content.rstrip("\n")
        # Reabre para escrita e adiciona exatamente uma linha em branco
        with open(file_path, "w", encoding="utf-8") as file_handle:
            if stripped_content:
                file_handle.write(stripped_content + "\n\n")  # garante uma linha em branco
            file_handle.write(content_to_write)
    else:
        with open(file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(content_to_write)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file.txt]")
        sys.exit(1)

    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        next_flags = [i for i, a in enumerate(args) if a in ("-f",) and i > d_index]
        end_index = next_flags[0] if next_flags else len(args)
        dirs = args[d_index + 1:end_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            print("Error: Missing file name after -f")
            sys.exit(1)
        file_name = args[f_index + 1]

    dir_path = os.path.join(*dirs) if dirs else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name
        lines = get_content()
        write_file(file_path, lines)
    else:
        print("No file specified. Only directories were created.")


if __name__ == "__main__":
    main()
