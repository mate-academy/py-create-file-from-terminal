from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import Sequence


def parse_args(args: Sequence[str]) -> tuple[list[str], str | None]:
    """Lê e interpreta os argumentos da linha de comando.

    Retorna:
        (lista_de_diretorios, nome_arquivo_ou_None)

    Exemplos de args (sem o nome do script):
        ["-d", "dir1", "dir2"]
        ["-f", "file.txt"]
        ["-d", "dir1", "dir2", "-f", "file.txt"]
    """
    directories: list[str] = []
    filename: str | None = None

    index = 0
    while index < len(args):
        arg = args[index]

        if arg == "-d":
            # Depois de "-d" vem uma sequência de nomes de diretório
            # até aparecer outra flag (começando com "-") ou acabar a lista.
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                directories.append(args[index])
                index += 1
            continue

        if arg == "-f":
            # Depois de "-f" esperamos exatamente um nome de arquivo.
            index += 1
            if index >= len(args) or args[index].startswith("-"):
                raise ValueError("Faltou o nome do arquivo após a flag -f.")
            filename = args[index]
            index += 1
            continue

        # Qualquer coisa diferente de -d ou -f aqui é argumento inesperado.
        raise ValueError(f"Argumento inesperado: {arg}")

    # Se não tem diretórios nem arquivo, o usuário chamou errado.
    if not directories and filename is None:
        raise ValueError("Você deve passar as flags -d e/ou -f.")

    return directories, filename


def build_directory_path(directories: Sequence[str]) -> str:
    """Monta o caminho absoluto do diretório a partir do diretório atual.

    Se não houver diretórios, devolve apenas o diretório atual.
    """
    base_dir = os.getcwd()
    if not directories:
        return base_dir
    # Ex.: cwd + "dir1" + "dir2" => ./dir1/dir2
    return os.path.join(base_dir, *directories)


def ensure_directories(path: str) -> None:
    """Garante que o diretório exista, criando se for necessário."""
    # exist_ok=True não dá erro se a pasta já existir.
    os.makedirs(path, exist_ok=True)


def read_content_lines(stop_word: str = "stop") -> list[str]:
    """Lê linhas digitadas pelo usuário até que ele digite a palavra de parada.

    Retorna uma lista com as linhas na mesma ordem digitada.
    """
    lines: list[str] = []

    while True:
        line = input("Enter content line: ")
        # strip() remove espaços extra, assim "stop " também para.
        if line.strip() == stop_word:
            break
        lines.append(line)

    return lines


def write_content(file_path: str, lines: Sequence[str]) -> None:
    """Escreve no arquivo um bloco com timestamp e linhas numeradas.

    Se o arquivo já existir e tiver conteúdo, adiciona uma linha em branco
    antes do novo bloco.
    """
    if not lines:
        # Se o usuário só digitou "stop" direto, não faz sentido escrever nada.
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verifica se o arquivo já existe E se não está vazio.
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    # "a" (append) => adiciona no final do arquivo, sem apagar conteúdo anterior.
    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            # Se já tinha conteúdo, separa o bloco anterior do novo
            # com uma linha em branco.
            file.write("\n")

        # Escreve o timestamp na primeira linha do bloco.
        file.write(f"{timestamp}\n")

        # Enumera a partir de 1: 1, 2, 3...
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


def main() -> None:
    """Função principal: orquestra a leitura de args, criação de pasta e arquivo."""
    try:
        # sys.argv[0] é o nome do script.
        # sys.argv[1:] são os argumentos que o usuário passou.
        directories, filename = parse_args(sys.argv[1:])
    except ValueError as error:
        # Mensagem de erro amigável + ajuda de uso.
        print(error)
        print(
            "Uso correto:\n"
            "  python create_file.py -d dir1 dir2\n"
            "  python create_file.py -f file.txt\n"
            "  python create_file.py -d dir1 dir2 -f file.txt",
        )
        return

    # Se o usuário passou diretórios, construímos o caminho e criamos.
    if directories:
        dir_path = build_directory_path(directories)
        ensure_directories(dir_path)
    else:
        # Caso não tenha diretórios, usamos o diretório atual.
        dir_path = os.getcwd()

    # Se não tiver filename, é o caso de "só criar pasta" (-d).
    if filename is None:
        return

    # Monta o caminho completo do arquivo.
    file_path = os.path.join(dir_path, filename)

    # Lê as linhas que o usuário digitar até "stop".
    content_lines = read_content_lines()

    # Escreve no arquivo no formato definido (timestamp + linhas numeradas).
    write_content(file_path, content_lines)


if __name__ == "__main__":
    # Ponto de entrada do script quando rodado diretamente pelo Python.
    main()
