import os
import sys
from datetime import datetime


def get_arguments() -> tuple[str, str]:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_idx = args.index("-d")
        # Encontra o fim dos argumentos de diretório (próxima flag ou fim da lista)
        f_idx = args.index("-f") if "-f" in args else len(args)
        
        # Define o intervalo correto dependendo da ordem das flags
        if "-f" in args and args.index("-f") < d_idx:
            path_parts = args[d_idx + 1:]
        else:
            path_parts = args[d_idx + 1:f_idx]
            
        dir_path = os.path.join(*path_parts) if path_parts else ""

    if "-f" in args:
        f_idx = args.index("-f")
        # Correção 1: Verifica se existe um nome de arquivo após a flag -f
        if f_idx + 1 < len(args):
            file_name = args[f_idx + 1]

    return dir_path, file_name


def get_content_from_user() -> str:
    content_lines = []
    line_num = 1
    
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{line_num} {line}")
        line_num += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Formatação conforme o exemplo: timestamp + conteúdo numerado
    return timestamp + "\n" + "\n".join(content_lines) + "\n"


def write_to_file(dir_path: str, file_name: str, content: str) -> None:
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    full_path = os.path.join(dir_path, file_name)
    
    # Correção 3: Adiciona linha em branco apenas se o arquivo já existir
    file_exists = os.path.exists(full_path)
    
    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(content)


def main() -> None:
    dir_path, file_name = get_arguments()

    # Correção 2: A lógica de conteúdo só roda se um NOME de arquivo foi passado
    if file_name:
        content = get_content_from_user()
        write_to_file(dir_path, file_name, content)
    elif dir_path:
        # Se apenas -d for passado, apenas cria os diretórios
        os.makedirs(dir_path, exist_ok=True)


if __name__ == "__main__":
    main()
