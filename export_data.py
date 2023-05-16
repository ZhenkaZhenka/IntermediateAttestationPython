def show_notes():
    notes = get_notes()
    for i in notes:
        print(get_text(i))


def get_notes():
    temp_str = ''
    with open('notes.json', 'r', encoding="utf-8") as notes:
        for i in notes:
            temp_str += i
    temp_list = temp_str.split('}')
    temp_list.remove("")
    list_of_notes = get_list_of_notes(temp_list)
    return sorted(list_of_notes, key=lambda x: x['date'], reverse=True)


def get_list_of_notes(list):
    list_of_dicts = []
    for i in range(len(list)):
        list_of_dicts.append(string_to_dict(list[i]))
    return list_of_dicts


def get_text(dict):
    text = ''
    for i in dict.keys():
        text += dict[i] + '\n'
    return text


def string_to_dict(text):
    dict = {}
    list = text.split(', ')
    for i in range(len(list)):
        temp = list[i]
        key = temp[:temp.index(':')].replace('{','').replace('"','')
        value = temp[temp.index(':')+2:].replace('"','')
        dict[key] = value
    return dict
