import sys
import os
from datetime import datetime


def get_user_content() -> list[str]:
    """Pobiera zawartość od użytkownika, dopóki nie wpisze 'stop'."""
    print("\n(wpisz 'stop' i Enter, aby zakończyć):")
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_content(content_lines: list[str]) -> str:
    """
    Formatuje zawartość, dodając timestamp i numerację linii.
    Usunięto końcowy '\\n' (odpowiedzialność za separację przeniesiono
    do funkcji write_content_to_file).
    """

    # Formatowanie timestampa
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    current_timestamp = datetime.now().strftime(timestamp_format)

    # Dodanie timestampa jako pierwszej linii
    formatted_content = [current_timestamp]

    # Dodanie numeracji do linii wprowadzonych przez użytkownika
    for i, line in enumerate(content_lines, 1):
        formatted_content.append(f"{i} {line}")

    # Zwrócenie sformatowanego bloku BEZ końcowej nowej linii
    return "\n".join(formatted_content)


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
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
                # W przypadku błędu parsowania flagi -f
                print("Błąd: Flaga -f wymaga podania nazwy pliku.")
                return [], None
        except ValueError:
            pass

    return dir_parts, file_name


def create_directories(dir_parts: list[str]) -> str | None:
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
    else:
        return "."  # Bieżący katalog

    try:
        # os.makedirs tworzy katalogi rekursywnie
        os.makedirs(target_dir, exist_ok=True)
        print(f"Utworzono katalog: {target_dir}")
        return target_dir
    except OSError as e:
        print(f"Błąd podczas tworzenia katalogu {target_dir}: {e}")
        return None


def write_content_to_file(file_path: str) -> None:
    """
    Pobiera zawartość od użytkownika, formatuje ją i zapisuje do pliku.
    Warunkowo dodaje nową linię jako separator przed dopisywaną zawartością,
    jeśli plik już istnieje i nie jest pusty.
    """
    content_lines = get_user_content()

    if not content_lines:
        return

    formatted_content = format_content(content_lines)

    should_add_separator = (os.path.exists(file_path)
                            and os.path.getsize(file_path) > 0)

    try:
        # Otwarcie pliku w trybie dopisywania ('a')
        with open(file_path, "a") as f:

            # Dodanie nowej linii jako separatora, jeśli plik jest już używany
            if should_add_separator:
                # Wymagane jest, aby nowy blok zaczynał się w nowej linii
                f.write("\n")

            f.write(formatted_content + "\n")
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


if __name__ == "__main__":
    create_file_app()
