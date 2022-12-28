import sys


def txt_importer(path_file):
    try:
        if '.txt' not in path_file:
            return print('Formato inválido', file=sys.stderr)

        with open(path_file, encoding="utf8") as file:
            data = file.read()
            lines = [line for line in data.split("\n")]
            return lines

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
