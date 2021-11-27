# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#[
#    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    count = int(input("введите, какое количество товаров вы хотете ввести"))
    n = 1
    _dict = []
    _list = []
    _analys = [{'название':[],'цена':[],'количество':[],'ед':[]}]
    while n <= count:
        _dict = dict({
            'название': input('Введите название товара'), 'цена': input('Введите цену товара'),
            'количество': input('Введите количество товара'), 'ед': input('Ввдите единицу измерения')})
        _list.append((n, _dict))
        n += 1
    for i in range(len(_list)):
        _analys[0]['название'].append(_list[i][1]['название'])
        _analys[0]['цена'].append(_list[i][1]['цена'])
        _analys[0]['количество'].append(_list[i][1]['количество'])
        if _list[i][1]['ед'] not in _analys[0]['ед']:
            _analys[0]['ед'].append(_list[i][1]['ед'])
    print(_list)
    print(_analys)