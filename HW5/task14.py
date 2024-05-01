"""
Создайте функцию генератор чисел Фибоначчи
"""
# Вариант 1 -  С заданным числом Фибоначи
def fibonachi(n):
    a, b = 0, 1 
    for _ in range(n):
        yield a
        a, b = b, a + b
        
data = list(fibonachi(10))
print(data)   

# Вариант 1 - Задаем число в командной строке 
a = int(input('введите число  '))

def fibonachi(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonachi(a)))