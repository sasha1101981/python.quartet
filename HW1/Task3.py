"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint
 
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
n = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt = 0

while True:
    print("Я загадал число от 1 до 1000, угадай его :)")
    user_num = int(input("Ваша догадка: "))
    attempt += 1
    if user_num == n:
        print(f"Ты угадал число, молодец!\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
        break
    elif user_num > n:
        print("Моё число меньше.")
    elif user_num < n:
        print("Моё число больше")



    