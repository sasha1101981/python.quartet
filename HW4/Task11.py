# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочно
# Любое действие выводит сумму денег
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)

# Функция меню
def menu():
    dct = {'1': 'Пополнить счет',
           '2': 'Снять со счета',
           '3': 'Выйти из программы'}
    
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)

# Функция выбора меню
def select_an_operation(balance: Decimal, count: int, is_flag: bool):
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)

    choice = input('Введите команду: ')
    if choice == '3':
        print(balance)
        is_flag = False
        return balance, is_flag
    elif choice == '1':
        balance = give_money(balance)
        count += 1
    elif choice == '2':
        balance = get_money(balance)
        count += 1
    else:
        print('Неверная команда')
    if count % 3 == 0:
        balance *= (1 + BONUS)

    print(balance)
    return balance, is_flag

# Функция снятия суммы
def get_money(balance: Decimal):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств для снятия')
            return balance

    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50')
        return balance

# Функция пополнения суммы
def give_money(balance: Decimal):
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        return balance + money_to_give
    else:
        print('Недостаточно средств для пополнения, сумма не кратна 50')
        return balance

def run():
    balance = 0
    count = 1
    is_flag = True
    while is_flag:
        menu()
        balance, is_flag = select_an_operation(balance, count, is_flag)
         
def main():
    run()

if __name__ == '__main__': 
    main()
