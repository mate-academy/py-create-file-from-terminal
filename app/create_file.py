import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv
    directory_path = ""
    file_name = ""

    # 1. Parsear argumentos de la terminal
    if "-d" in args:
        d_index = args.index("-d")
        # Buscamos hasta el siguiente flag o el final de la lista
        path_parts = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            path_parts.append(arg)
        directory_path = os.path.join(*path_parts) if path_parts else ""

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    # 2. Crear directorios si es necesario
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    # 3. Recopilar contenido de forma interactiva
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # 4. Preparar la ruta final y el bloque de contenido
    full_path = os.path.join(directory_path, file_name) if file_name else ""

    if full_path:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Abrimos en modo 'a' (append) para añadir al final si ya existe
        with open(full_path, "a") as file:
            file.write(f"{timestamp}\n")
            for index, line in enumerate(content_lines, start=1):
                file.write(f"{index} {line}\n")
            file.write("\n")  # Espacio extra entre bloques de contenido


if __name__ == "__main__":
    create_file()
