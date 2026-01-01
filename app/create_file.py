import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    # 1. Parsing dos argumentos (sys.argv)
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Coleta itens após -d até encontrar outra flag ou acabar
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue
        else:
            i += 1

    # 2. Criar diretórios (os.makedirs)
    target_dir = "."
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)

    # 3. Se não houver nome de arquivo, apenas encerra
    if not file_name:
        return

    # 4. Ler entrada de conteúdo do usuário
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    # 5. Preparar o bloco de texto
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_block = [timestamp]

    for idx, line in enumerate(content_lines, start=1):
        formatted_block.append(f"{idx} {line}")

    full_content = "\n".join(formatted_block)

    # 6. Escrever no arquivo (os.path.join)
    file_path = os.path.join(target_dir, file_name)
    file_exists = os.path.exists(file_path)

    # 'a' (append) cria o arquivo ou adiciona ao final
    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            # Adiciona linha em branco antes do bloco se o arquivo já existir
            f.write("\n\n")
        f.write(full_content)


if __name__ == "__main__":
    main()
