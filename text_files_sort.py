import os

def create_combined_list(directory):
    """Функция для создания комбинированного списка из полученных текстовых файлов в указанной директории"""
    file_list = os.listdir(directory)
    combined_list = []
    # Перебираем каждый файл в списке имен файлов
    for file in file_list:
        with open(directory + "/" + file, encoding='utf-8') as f:
            # Формируем комбинированный список по принципу: имя файла, кол-во строк, список из строк файла
            combined_list.append([file, 0 , []])
            for line in f:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1
    # Возвращаем отсортированный по количеству строк список начиная с меньшего
    return sorted(combined_list, key= lambda x: x[2], reverse = True)

def create_file_from_directory(directory, filename):
    """Функция для создания отсортированного текстового файла из всех полученных текстовых файлов в папке"""
    with open(filename + '.txt', 'w+', encoding='utf-8') as newfile:
        # Перебираем полученный с помощью функции сортированный список и формируем файл в требуемом формате
        for file in create_combined_list(directory):
            newfile.write(f'{file[0]}\n')
            newfile.write(f'{file[1]}\n')
            for string in file[2]:
                newfile.write(string)
                newfile.write('\n')

create_file_from_directory('text', 'sorted_text')