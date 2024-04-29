# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def thesaurus(*args):
    name_list = [*args]
    dictionary = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in dictionary.keys():
            dictionary[capital].append(name)
        else:
            dict_1 = [name]    
            dictionary[capital] = dict_1
    return dictionary
print(thesaurus("Miky", "Marse", "Luke", "Pyper", "Any", "Bred", "Anton", ))        



