# -----------------------------------------------------------------------------------
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
# -----------------------------------------------------------------------------------
def types_list(list):
    for i in range(len(list)):
        print(f'{i} элемент списка - {list[i]} имеет тип {type(list[i])}')
if __name__ == '__main__':
    list = [2, '12', b'\x8b', ('1', '2'), [1,4,5,6], 2.45 , True]
    types_list(list)