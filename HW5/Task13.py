"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
 - имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""

names = ['Vlad', 'Alex' ,'Katy']
salaries = [500000, 600000, 700000]
bonuses = ['10%', '7.25%', '5%']
print(f'исходные данные:\n{names}\n{salaries}\n{bonuses}')
print({name: salary * float(bonus[:-1]) / 100 for name, salary, bonus in zip(names, salaries, bonuses)})














        
        
        
        

        






