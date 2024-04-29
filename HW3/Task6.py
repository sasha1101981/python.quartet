# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

"""
import collections

lst = [21,25,24,54,45,21,25,56,24]

new_lst = collections.Counter(lst)
print(dict(new_lst))
"""

lst = [21,25,24,54,45,21,25,56,24]

new_lst = filter(lambda x: lst.count(x) > 1, lst)
new_lst = list(set(new_lst))

print(new_lst)


