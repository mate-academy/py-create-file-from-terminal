"""Module to create files and directories from command line arguments."""

from datetime import datetime
import os
import sys
from typing import List, Optional, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], Optional[str]]:
    """Parse command line arguments for directories and filename."""
    dirs: List[str] = []
    filename: Optional[str] = None

    i = 1
    while i < len(args):
        arg = args[i]
        if arg in ("-d", "--dir"):
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue
        elif arg in ("-f", "--file"):
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            continue
        else:
            if not filename and ("." in arg or len(args) == 2):
                filename = arg
            else:
                dirs.append(arg)
            i += 1

    return dirs, filename


def main() -> None:
    """Execute main program logic."""
    dirs, filename = parse_arguments(sys.argv)

    target_dir = ""
    if dirs:
        target_dir = os.path.join(*dirs)
        os.makedirs(target_dir, exist_ok=True)

    if not filename:
        if dirs:
            print(f"Diretório '{target_dir}' criado com sucesso.")
        return

    file_path = (
        os.path.join(target_dir, filename) if target_dir else filename
    )

    content_lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)
        except EOFError:
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_entry_parts = [timestamp]
    for idx, line in enumerate(content_lines, 1):
        new_entry_parts.append(f"{idx} {line}")

    new_content = "\n".join(new_entry_parts) + "\n"

    file_exists = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    mode = "a" if file_exists else "w"

    with open(file_path, mode, encoding="utf-8") as file_obj:
        if file_exists:
            file_obj.write("\n")
        file_obj.write(new_content)

    print(f"Arquivo '{file_path}' atualizado com sucesso!")


if __name__ == "__main__":
    main()
