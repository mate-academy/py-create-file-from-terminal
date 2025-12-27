import sys
import os
from datetime import datetime


def make_directory(directory: list[str]) -> str:
    if directory is None:
        return ""
    cleared_segments = [s for s in directory if s.strip()]
    if cleared_segments:
        path = os.path.join(*cleared_segments)
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    return path


def write_file(path: str, file_name: str) -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath = os.path.join(path, file_name)

    exist = os.path.exists(filepath) and os.path.getsize(filepath) > 0
    with open(filepath, "a", encoding="utf-8") as source_file:
        if exist:
            source_file.write("\n")
        line_numeration = 1
        source_file.write(date + "\n")
        while True:
            line = input("Enter content line: ").strip()
            if line == "":
                continue
            if line.strip().lower() == "stop":
                break
            source_file.write(f"{line_numeration} {line}\n")
            line_numeration += 1


def create_file() -> None:
    args: list[str] = sys.argv[1:]
    directory_segments = []
    file_name = None
    i = 0
    while i < len(args):
        arg = args[i]

        if arg in ("-d", "--directory"):
            i += 1
            temp_segments = []
            while i < len(args) and not args[i].startswith("-"):
                temp_segments.append(args[i])
                i += 1

            if temp_segments:
                directory_segments = temp_segments
            i -= 1

        elif arg in ("-f", "--file"):
            i += 1
            if i >= len(args):
                print("Błąd: Flaga -f wymaga podania nazwy pliku.")
                sys.exit(1)
            if args[i].startswith("-"):
                print(
                    "Błąd: Flaga -f musi mieć przypisaną nazwę pliku,"
                    "a nie kolejną flagę."
                )
                sys.exit(1)
            file_name = args[i]
    i += 1

    path = make_directory(directory_segments)
    if file_name is not None:
        write_file(path, file_name)
    else:
        print(
            "\nArgument -f nie został podany."
            "Zakończono tworzenie samej struktury katalogów."
        )


if __name__ == "__main__":
    create_file()
