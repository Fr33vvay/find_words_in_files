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
    count = 0  # Совпавшие строки
    try:
        with open(file, encoding='windows-1251') as f, open('strings.txt', 'a') as new_file:
            for line in f:
                if word in line:
                    if line[-1] != '\n':
                        line += '\n'
                    count += 1
                    new_file.write(line)
    except UnicodeDecodeError:
        print(f'Ошибка кодировки в {file}')
    return count


def search_files(folder):
    """Ищет слово во всех txt-файлах в указанной папке"""
    sum_count = 0
    for query in query_list():
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in [f for f in filenames if f.endswith(".txt")]:
                sum_count += search_word(query, os.path.join(dirpath, filename))
    print(f'Найдено {sum_count} строк.')


if __name__ == '__main__':
    search_files(input('Введите адрес папки: '))