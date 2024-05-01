"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
"""
import os

from os import path
file_path = os.path.abspath("D:\GeekBrain\3 quarter\Python-diving\python.quartet\HW5\Task12.py")
name = os.path.basename("D:\GeekBrain\3 quarter\Python-diving\python.quartet\HW5\Task12.py")
expansion = path.splitext(file_path)[1]
print(file_path)
print(name)
print(expansion)
print(f'Исходная строка: {file_path}, {name} ,{expansion}')
"""
import os

file_path = "D:\GeekBrain\3 quarter\Python-diving\python.quartet\HW5\Task12.py"
def fun(file_path: str) -> tuple:
    path, filename = os.path.split(file_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {file_path} \nКортеж из пути: {fun(file_path)}')