import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:
    """Parse command line args and return (dir_parts, filename)."""
    args = argv[:]
    dir_parts: List[str] = []
    filename: Optional[str] = None

    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None

    if f_index is not None:
        if f_index + 1 < len(args) and args[f_index + 1] not in ("-d", "-f"):
            filename = args[f_index + 1]
        else:
            raise ValueError("Flag -f fornecido sem um nome de arquivo.")

    if d_index is not None:
        end_slice = len(args)
        if f_index is not None and f_index > d_index:
            end_slice = f_index
        dir_parts = args[d_index + 1:end_slice]
        if not dir_parts:
            raise ValueError("Flag -d fornecido sem um caminho de diretório.")

    if not dir_parts and not filename:
        raise ValueError(
            "Nenhum argumento fornecido. Use -d para diretório "
            "e -f para nome de arquivo."
        )

    return dir_parts, filename


def ensure_directory(dir_parts: List[str]) -> str:
    """Create and return the target directory path."""
    if not dir_parts:
        return "."
    target_path = os.path.join(*dir_parts)
    os.makedirs(target_path, exist_ok=True)
    print(f"Diretório criado/assegurado: {target_path}")
    return target_path


def write_content(full_path: str) -> None:
    """Append timestamp and user lines to the file.
    Adds a separating blank line only if the file already has content.
    """
    file_exists = os.path.exists(full_path)
    non_empty = file_exists and os.path.getsize(full_path) > 0

    with open(full_path, "a", encoding="utf-8") as file_obj:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        if non_empty:
            file_obj.write("\n")
        file_obj.write(f"{timestamp}\n")

        print("Enter content line (type 'stop' to finish):")
        line_number = 1
        while True:
            try:
                user_input = input("Enter content line: ")
            except EOFError:
                break
            if user_input.strip().lower() == "stop":
                break
            file_obj.write(f"{line_number} {user_input}\n")
            line_number += 1

    print(f"Conteúdo salvo com sucesso em: {full_path}")


def main() -> None:
    try:
        dir_parts, filename = parse_args(sys.argv[1:])
    except ValueError as exc:
        print(f"Erro: {exc}")
        sys.exit(1)

    target_path = ensure_directory(dir_parts)

    if not filename:
        return

    full_file_path = os.path.join(target_path, filename)
    print(f"Abrindo arquivo: {full_file_path}")
    write_content(full_file_path)