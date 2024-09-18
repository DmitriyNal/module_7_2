import pprint

def custom_write(file_name, strings):#
    strings_positions = {}# создаем пустой словарь для хранения позиций строк в файле
    with open(file_name, "w",encoding="utf8") as file:# открываем файл для записи
        for i,string in enumerate(strings, start=1):
            cursor = file.tell()# получаем позицию в файле
            file.write(string + '\n')# записываем строку в файл
            strings_positions[(i,cursor)] = string# сохраняем позицию строки в словаре
        return strings_positions



if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


















