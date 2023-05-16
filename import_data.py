from datetime import datetime as dt
import export_data as ed
import json


def create_note():
    dict = {'id': get_id()+1,
        'date': dt.now().strftime('%d.%m.%Y %H:%M'),
        'header': input('Введите заголовок заметки: '),
        'note': input('Введите заметку: ')}
    add_data(dict)
    print('Заметка добавлена успешно!')


def delete_note(index):
    list = ed.get_notes()
    list.remove(list[index])
    change_data(list)
    print('Заметка удалена успешно!')


def change_note(index, key):
    list = ed.get_notes()
    list[index][key] = input('Внесите изменения: ')
    list[index]['date'] = dt.now().strftime('%d.%m.%Y %H:%M')
    change_data(list)
    print('Изменения внесены успешно!')


def add_data(dict):
    with open('notes.json', 'a', encoding="utf-8") as notes:
        json.dump(dict, notes, ensure_ascii=False)


def change_data(list):
    with open('notes.json', 'w', encoding="utf-8") as notes:
        for i in list:
            json.dump(i, notes, ensure_ascii=False)


def get_id():
    max = 0
    temp_list = ed.get_notes()
    for i in temp_list:
        if int(i['id']) > max:
            max = int(i['id'])
    return max

