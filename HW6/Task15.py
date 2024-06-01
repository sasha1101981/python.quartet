"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.  
 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
 Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
 Проверку года на високосность вынести в отдельную защищённую функцию"""

from datetime import datetime as dt
from calendar import isleap

def check_date(date: str):
    try:
        is_year  = dt.strptime(date, "%d.%m.%Y")
        validator_date(is_year.year)
        return True
    except:
        return False

def validator_date(year: int):
    print(f"Год явлениется: Высокосным " if isleap(year) else f"Год явлениется: НЕ Высокосным")

def run():
    date = input("Введите дату: ")
    print(f"Дата введена корректно?", check_date(date))

if __name__ == '__main__':
    run()