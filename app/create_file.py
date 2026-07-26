import sys
import os
from datetime import datetime

# Pobranie argumentów (bez nazwy pliku .py)
args = sys.argv[1:]

path_parts = []
file_name = None

# Sprawdzenie, czy podano -d (ścieżka do katalogu)
if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        path_parts = args[d_index + 1:f_index]
    else:
        path_parts = args[d_index + 1:]

# Sprawdzenie, czy podano -f (nazwa pliku)
if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

# Utworzenie ścieżki katalogu (jeśli podano -d)
directory_path = os.path.join(*path_parts) if path_parts else None

# Utworzenie pełnej ścieżki do pliku
full_path = os.path.join(directory_path, file_name) \
    if directory_path else file_name

# Utworzenie katalogu, jeśli istnieje
if directory_path:
    os.makedirs(directory_path, exist_ok=True)

# Wczytywanie linii od użytkownika
lines = []
line_number = 1

while True:
    user_input = input("Enter content line: ")
    if user_input.lower() == "stop":
        break
    lines.append(f"{line_number} {user_input}")
    line_number += 1

# Tworzenie bloku tekstowego z timestampem i treścią
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
block = [timestamp] + lines
block_content = "\n".join(block) + "\n\n"

# Dopisanie do pliku (tworzy nowy, jeśli nie istnieje)
with open(full_path, "a", encoding="utf-8") as f:
    f.write(block_content)
