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


def get_file_app() -> None:
    """Główna funkcja aplikacji do tworzenia plików i katalogów."""

    # Sprawdzenie minimalnej liczby argumentów
    if len(sys.argv) < 3:
        return

    # --- 1. Parsowanie flag i argumentów ---

    dir_parts = []
    file_name = None

    # Flagi to: -d (katalogi), -f (nazwa pliku)

    # Szukanie flag -d i -f
    if "-d" in sys.argv:
        try:
            d_index = sys.argv.index("-d")
            for i in range(d_index + 1, len(sys.argv)):
                if sys.argv[i].startswith("-"):
                    break
                dir_parts.append(sys.argv[i])
        except ValueError:
            pass

    if "-f" in sys.argv:
        try:
            f_index = sys.argv.index("-f")
            # Następny argument po -f to nazwa pliku
            if (f_index + 1 < len(sys.argv) and not
                    sys.argv[f_index + 1].startswith("-")):
                file_name = sys.argv[f_index + 1]
            else:
                print("Błąd: Flaga -f wymaga podania nazwy pliku.")
                return
        except ValueError:
            pass  # Jeśli -f nie znaleziono

    # Sprawdzenie, czy nazwa pliku została podana, jeśli użyto flagi -f
    if "-f" in sys.argv and file_name is None:
        return

    # --- 2. Tworzenie ścieżki i katalogów ---

    # Zbudowanie ścieżki do katalogu
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
    else:
        target_dir = "."  # Bieżący katalog

    # Jeśli podano katalogi, utwórz je (zagnieżdżone)
    if target_dir != ".":
        try:
            # os.makedirs tworzy katalogi rekursywnie (jak `mkdir -p`)
            os.makedirs(target_dir, exist_ok=True)
            print(f"Utworzono katalog: {target_dir}")
        except OSError as e:
            print(f"Błąd podczas tworzenia katalogu {target_dir}: {e}")
            return

    # --- 3. Tworzenie i zapisywanie pliku ---

    if file_name:
        # Pełna ścieżka do pliku
        file_path = os.path.join(target_dir, file_name)

        # Pobranie sformatowanej zawartości od użytkownika
        content_lines = get_user_content()
        if not content_lines:
            return

        formatted_content = format_content(content_lines)

        # Otwarcie pliku w trybie dopisywania ('a')
        # Jeśli plik istnieje, zawartość zostanie dopisana na końcu.
        # Jeśli plik nie istnieje, zostanie utworzony (analogicznie do 'w').
        try:
            with open(file_path, "a") as f:
                f.write(formatted_content)
            print(f"\nSukces: Zawartość zapisana do pliku {file_path}")

        except IOError as e:
            print(f"Błąd podczas zapisu do pliku {file_path}: {e}")

    else:
        print("Nie podano flagi -f. Utworzono tylko katalog.")
