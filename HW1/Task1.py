"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны 
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним."""

a = int(input(f'Сторона a : '))
b = int(input(f'Сторона b : '))
c = int(input(f'Сторона c : '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Равносторонний треугольник')
    
    elif a == b and b != c and a != c:
        print('Равнобедренный треугольк')    
    
    elif a != b and b != c and a != c:
        print('Разностороннй треуголик')
else:
        print('Треугольник с такими сторонами не существует.')  
        