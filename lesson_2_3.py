# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

if __name__ == '__main__':
    list_mounth = [[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
    mounth = int(input('Введите цесяц в виде целого числа: '))
    season = {1: 'Зима',    2:'Весна',    3:'Лето',    4:'Осень'}
    for i in range(4):
        if mounth in list_mounth[i]:
            print(f'Этот месяц относится к времени года - {season[i+1]}')
