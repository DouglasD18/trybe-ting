from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def create_dict(path, line, instance: Queue()):
    line_dict = {
        "nome_do_arquivo": path,
        "qtd_linhas": len(line),
        "linhas_do_arquivo": line,
    }
    instance.enqueue(line_dict)
    print(line_dict, file=sys.stdout)


def process(path_file, instance: Queue()):
    line = txt_importer(path_file)
    if len(instance) == 0:
        create_dict(path_file, line, instance)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
