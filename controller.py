import import_data as id
import export_data as ed

def action():
    action = input('Добро пожаловать в заметки, выберите действие:\n'
          '1. Создать заметку\n'
          '2. Редактировать заметку\n'
          '3. Удалить заметку\n'
          '4. Посмотреть все заметки\n'
          '5. Не хочу ничего смотреть, до свидания!\n')
    match(action):
        case '1':
            id.create_note()
            return True
        case '2':
            changing_note()
            return True
        case '3':
            deleting_note()
            return True
        case '4':
            ed.show_notes()
            return True
        case '5':
            print('До новых встреч!')
            return False
        case _:
            print('Такого действия нет, попробуйте еще')
            return True


def start():
    mark = True
    while(mark):
        mark = action()


def changing_note():
    if checking_notes():
        ed.show_notes()
        id.change_note(get_index('Введите id заметки для изменения: '),
                       get_pitch('Введите поле для изменения:\n'
                             'header\n'
                             'note\n '))
    else:
        print('Список пуст, для редактирования создайте что-нибудь')


def deleting_note():
    if checking_notes():
        ed.show_notes()
        id.delete_note(get_index('Введите id заметки для удаления: '))
    else:
        print('Список пуст, для удаление создайте что-нибудь')


def checking_notes():
    if len(ed.get_notes()) != 0:
        return True
    else:
        return False


def get_pitch(message):
    while(True):
        pitch = input(message)
        if (pitch == "header" or pitch == "note"):
            return pitch
        else:
            print('Возможно вы ошиблись в написании поля, попробуйте еще')

def get_index(message):
    list = ed.get_notes()
    while True:
        id = input(message)
        index = get_id(list, id)
        if index == -1:
            print('Такого id нет')
        else:
            return index


def get_id(list, id):
    for i in list:
        if i['id'] == id:
            return list.index(i)
    return -1