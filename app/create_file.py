import datetime
import os
import sys


def create_file(file_name: str, directories: str) -> None:
    # Criar diretórios se necessário
    if directories is not None and directories != []:
        path = os.path.join(*directories)
        full_path = os.path.join(path, file_name)
        os.makedirs(path, exist_ok=True)
    else:
        full_path = file_name
    # Verificar se arquivo existe para saber quantas linhas já tem
    existing_lines = 0
    if os.path.exists(full_path):
        with open(full_path, "r") as f:
            # Contar linhas numeradas existentes
            for line in f:
                if line.strip() and line[0].isdigit():
                    try:
                        line_num = int(line.split()[0])
                        existing_lines = max(existing_lines, line_num)
                    except (ValueError, IndexError):
                        pass
    # Coletar conteúdo do usuário
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    # Escrever no arquivo
    with open(full_path, "a") as f:
        # Adicionar timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        # Adicionar linhas numeradas
        for i, line in enumerate(lines, start=existing_lines + 1):
            f.write(f"{i} {line}\n")
        # Adicionar linha em branco no final
        f.write("\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)
    directories = []
    file_name = None
    # Parsear argumentos
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            # Coletar todos os diretórios até encontrar -f ou fim
            i += 1
            while i < len(sys.argv) and sys.argv[i] != "-f":
                directories.append(sys.argv[i])
                i += 1
        elif sys.argv[i] == "-f":
            # Próximo argumento é o nome do arquivo
            i += 1
            if i < len(sys.argv):
                file_name = sys.argv[i]
                i += 1
        else:
            i += 1
    # Validar que temos pelo menos um filename se -f foi usado
    if file_name is None or file_name == "":
        print("Error: File name is required with -f flag")
        sys.exit(1)
    # Criar o arquivo
    create_file(file_name, directories if directories else None)


if __name__ == "__main__":
    main()
