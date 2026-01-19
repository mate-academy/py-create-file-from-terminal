import datetime
import os
import sys


def create_file(file_name: str, directories: dict) -> None:
    # Criar diretórios se necessário
    if directories is not None and directories != []:
        path = os.path.join(*directories)
        full_path = os.path.join(path, file_name)
        os.makedirs(path, exist_ok=True)
    else:
        full_path = file_name
    # Verificar se arquivo existe para saber quantas linhas já tem
    if os.path.exists(full_path):
        with open(full_path, "r") as file_handle:
            # Contar linhas numeradas existentes
            for line in file_handle:
                if line.strip() and line[0].isdigit():
                    try:
                        int(line.split()[0])
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
    with open(full_path, "a") as file_handle:
        # Adicionar timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_handle.write(f"{timestamp}\n")
        # Adicionar linhas numeradas (FIXED: now starts from 1)
        for line_num, line in enumerate(lines, start=1):
            file_handle.write(f"{line_num} {line}\n")
        # Adicionar linha em branco no final
        file_handle.write("\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)
    directories = []
    file_name = None
    # Parsear argumentos
    arg_index = 1
    while arg_index < len(sys.argv):
        if sys.argv[arg_index] == "-d":
            # Coletar todos os diretórios até encontrar -f ou fim
            arg_index += 1
            while arg_index < len(sys.argv) and sys.argv[arg_index] != "-f":
                directories.append(sys.argv[arg_index])
                arg_index += 1
        elif sys.argv[arg_index] == "-f":
            # Próximo argumento é o nome do arquivo
            arg_index += 1
            if arg_index < len(sys.argv):
                file_name = sys.argv[arg_index]
                arg_index += 1
        else:
            arg_index += 1

    # If only directories are provided, create them and exit
    if file_name is None and directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
        return

    # Validar que temos pelo menos um filename se -f foi usado
    if file_name is None or file_name == "":
        print("Error: File name is required with -f flag")
        sys.exit(1)
    # Criar o arquivo
    create_file(file_name, directories if directories else None)


if __name__ == "__main__":
    main()
