import os
import sys
from datetime import datetime

# 1. Lecture de sys.argv
args = sys.argv[1:]

directories = []
filename = ""

if "-d" in args:
    idx_d = args.index("-d")
    for item in args[idx_d + 1:]:
        if item in ("-d", "-f"):
            break
        directories.append(item)

if "-f" in args:
    idx_f = args.index("-f")
    if idx_f + 1 < len(args):
        filename = args[idx_f + 1]


def save_to_file(file_path: str, block_to_write: str) -> None:
    """Fonction auxiliaire DRY pour gérer l'écriture et le mode append."""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n\n" + block_to_write)
    else:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(block_to_write)


# 2. Gestion des dossiers avec os.path.join
dir_path = os.path.join(*directories) if directories else None

if dir_path:
    os.makedirs(dir_path, exist_ok=True)

# 3. Écriture dans le fichier
if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    # L'horodatage est isolé sur sa première ligne
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_block = f"{timestamp}\n"

    # Ajout des lignes de contenu indexées
    for idx, content in enumerate(lines, start=1):
        if idx == len(lines):
            formatted_block += f"{idx} {content}"
        else:
            formatted_block += f"{idx} {content}\n"

    # Construction du chemin final via os.path.join
    full_file_path = os.path.join(dir_path, filename) if dir_path else filename

    # Appel de la fonction unique (Respect du principe DRY)
    save_to_file(full_file_path, formatted_block)
