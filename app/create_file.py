import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    # Lógica para extrair diretórios e nome do arquivo dos argumentos
    if "-d" in args:
        d_index = args.index("-d")
        # Encontra onde termina a lista de diretórios (próxima flag ou fim da lista)
        f_index = args.index("-f") if "-f" in args else len(args)
        
        # Se -f vier antes de -d, ajustamos a lógica de fatiamento
        if "-f" in args and args.index("-f") < d_index:
            path_parts = args[d_index + 1:]
        else:
            path_parts = args[d_index + 1:f_index]
            
        dir_path = os.path.join(*path_parts) if path_parts else ""

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    # Criação do diretório se necessário
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # Caminho completo do arquivo
    full_path = os.path.join(dir_path, file_name) if file_name else ""

    if full_path:
        content_lines = []
        line_num = 1
        
        # Coleta de conteúdo do terminal
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(f"{line_num} {line}")
            line_num += 1

        # Preparação do timestamp e bloco de conteúdo
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_content = timestamp + "\n" + "\n".join(content_lines) + "\n\n"

        # Escrita no arquivo (modo 'a' para anexar se já existir)
        with open(full_path, "a") as f:
            f.write(new_content)


if __name__ == "__main__":
    create_file()
