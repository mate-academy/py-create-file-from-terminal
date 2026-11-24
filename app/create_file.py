import os
import sys
from datetime import datetime


def parse_arguments(
    args: list[str],
) -> tuple[list[str], str | None]:
    """Parse command-line arguments for directories and file name."""
    dirs: list[str] = []
    file_name: str | None = None

    i = 1 if args and not args[0].startswith("-") else 0

    while i < len(args):
        arg = args[i]
        if arg == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif arg == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return dirs, file_name


def collect_content() -> list[str]:
    """Collect lines of content from terminal until 'stop' is entered."""
    lines: list[str] = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            break
    return lines


def main() -> None:
    dirs, file_name = parse_arguments(sys.argv)

    # 1. Criar diretórios
    dir_path = ""
    if dirs:
        dir_path = os.path.join(*(str(d) for d in dirs))
        os.makedirs(dir_path, exist_ok=True)

    if not file_name:
        return

    # 2. Definir o caminho completo do ficheiro
    target_path = (
        os.path.join(dir_path, file_name)
        if dir_path
        else file_name
    )

    # 3. Recolher o conteúdo via input
    lines = collect_content()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 4. Formatar o conteúdo
    formatted_lines = [timestamp]
    for idx, line in enumerate(lines, start=1):
        formatted_lines.append(f"{idx} {line}")

    new_content = "\n".join(formatted_lines) + "\n"

    # 5. Escrever ou fazer append no ficheiro
    file_exists = os.path.exists(target_path)
    mode = "a" if file_exists else "w"

    with open(target_path, mode, encoding="utf-8") as f:
        if file_exists:
            f.write("\n" + new_content)
        else:
            f.write(new_content)


if __name__ in ("__main__", "<run_path>"):
    main()
