from ting_file_management.queue import Queue


def exists_word(word, instance: Queue()):
    lower = word.lower()
    length = len(instance)
    lista = []
    for index in range(length):
        data = instance.search(index)
        lines = data["linhas_do_arquivo"]
        lines_number = []
        for number in range(len(lines)):
            if lower in lines[number].lower():
                lines_number.append(number + 1)

        if len(lines_number):
            lista.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [{"linha": number} for number in lines_number]
            })

    return lista


def search_by_word(word, instance):
    lower = word.lower()
    length = len(instance)
    lista = []
    for index in range(length):
        data = instance.search(index)
        lines = data["linhas_do_arquivo"]
        occurences = []
        for number in range(len(lines)):
            if lower in lines[number].lower():
                occurences.append({
                    "linha": number + 1,
                    "conteudo": lines[number]
                })

        if len(occurences):
            lista.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occurences
            })

    return lista
