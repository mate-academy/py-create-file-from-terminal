import sys
import os
from datetime import datetime


def get_user_content() -> list:
    """Pobiera zawartość od użytkownika, dopóki nie wpisze 'stop'."""
    print("\n(wpisz 'stop' i Enter, aby zakończyć):")
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_content(content_lines: list) -> str:
    """Formatuje zawartość, dodając timestamp i numerację linii."""

    # Formatowanie timestampa
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    current_timestamp = datetime.now().strftime(timestamp_format)

    # Dodanie timestampa jako pierwszej linii
    formatted_content = [current_timestamp]

    # Dodanie numeracji do linii wprowadzonych przez użytkownika
    for i, line in enumerate(content_lines, 1):
        formatted_content.append(f"{i} {line}")
    return "\n".join(formatted_content) + "\n"


def parse_arguments(args: list) -> any:
    dir_parts = []
    file_name = None

    # Uproszczone parsowanie flag -d
    if "-d" in args:
        try:
            d_index = args.index("-d")
            # Zbiera argumenty po -d
            for i in range(d_index + 1, len(args)):
                if args[i].startswith("-"):
                    break
                dir_parts.append(args[i])
        except ValueError:
            pass

    # Uproszczone parsowanie flag -f
    if "-f" in args:
        try:
            f_index = args.index("-f")
            if (f_index + 1 < len(args) and not
                    args[f_index + 1].startswith("-")):
                file_name = args[f_index + 1]
            else:
                return None, None
        except ValueError:
            pass

    return dir_parts, file_name


def create_directories(dir_parts: str) -> str:
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
    else:
        return "."  # Bieżący katalog

    try:
        os.makedirs(target_dir, exist_ok=True)
        print(f"Utworzono katalog: {target_dir}")
        return target_dir
    except OSError as e:
        print(f"Błąd podczas tworzenia katalogu {target_dir}: {e}")
        return None


def write_content_to_file(file_path: str) -> None:
    content_lines = get_user_content()

    if not content_lines:
        return

    formatted_content = format_content(content_lines)

    try:
        with open(file_path, "a") as f:
            f.write(formatted_content)
        print(f"\nSukces: Zawartość zapisana do pliku {file_path}")

    except IOError as e:
        print(f"Błąd podczas zapisu do pliku {file_path}: {e}")


def create_file_app() -> None:
    """Główna funkcja aplikacji, koordynująca mniejsze funkcje."""

    if len(sys.argv) < 3:
        return

    # 1. Parsowanie argumentów
    dir_parts, file_name = parse_arguments(sys.argv)

    if "-f" in sys.argv and file_name is None:
        return

    # 2. Tworzenie katalogów
    target_dir = create_directories(dir_parts)

    if target_dir is None:
        return

    # 3. Zapisywanie pliku
    if file_name:
        file_path = os.path.join(target_dir, file_name)
        write_content_to_file(file_path)
    elif dir_parts:
        print("Nie podano flagi -f. Utworzono tylko katalog.")
    else:
        # Ten przypadek jest rzadki, bo jest kontrolowany na początku
        print("Nie podano wystarczających argumentów.")
