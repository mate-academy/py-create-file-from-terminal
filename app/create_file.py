import sys
import os
from datetime import datetime

def parse_arguments(args):
    dirs = []
    filename = None
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg in ('-d', '--dir'):
            i += 1
            while i < len(args) and not args[i].startswith('-'):
                dirs.append(args[i])
                i += 1
            continue
        elif arg in ('-f', '--file'):
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            continue
        else:
            i += 1
            
    return dirs, filename

def main():
    dirs, filename = parse_arguments(sys.argv)
    
    # Se diretórios foram informados, cria a estrutura de diretórios
    target_dir = ""
    if dirs:
        target_dir = os.path.join(*dirs)
        os.makedirs(target_dir, exist_ok=True)
    
    # Se nenhum arquivo foi especificado, encerra após criar o diretório (caso `-d` tenha sido usado sozinho)
    if not filename:
        if dirs:
            print(f"Diretório '{target_dir}' criado com sucesso.")
        else:
            print("Nenhum diretório ou arquivo válido foi especificado.")
        return

    # Caminho completo do arquivo
    file_path = os.path.join(target_dir, filename) if target_dir else filename

    # Coleta as linhas de conteúdo do terminal até digitar "stop"
    content_lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)
        except EOFError:
            break

    # Gera o registro de data e hora formatado
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Monta o bloco de conteúdo com a data no topo e linhas numeradas
    new_entry_parts = [timestamp]
    for idx, line in enumerate(content_lines, 1):
        new_entry_parts.append(f"{idx} {line}")
    
    new_content = "\n".join(new_entry_parts) + "\n"

    # Escreve ou adiciona ao arquivo existente
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as f:
        f.write(new_content)

    print(f"Arquivo '{file_path}' atualizado com sucesso!")

if __name__ == "__main__":
    main()
