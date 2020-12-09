import os.path


def query_list():
    """Собирает список запросов поиска"""
    q_list = []
    query = input('Введите запросы. После каждого запроса нажмите Enter.'
                  'В конце введите точку (.): ')
    while query != '.':
        q_list.append(query)
        query = input()
    return q_list


def search_word(word, file):
    """Выписывает строки, содержащие искомое слово"""
    with open(file, encoding='windows-1251') as f, open('strings.txt', 'a') as new_file:
        for line in f:
            if word in line:
                new_file.write(line)


def search_files(folder):
    """Ищет слово во всех txt-файлах в указанной папке"""
    for query in query_list():
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in [f for f in filenames if f.endswith(".txt")]:
                search_word(query, os.path.join(dirpath, filename))


if __name__ == '__main__':
    search_files(input('Введите адрес папки: '))