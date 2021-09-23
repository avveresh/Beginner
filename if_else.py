# false, none, 0 и все пустые объекты считаются 'ложью'
# != не равно
a = 0
# отступы это синтаксис Python
if a == 5:
    print('a равно 5')
elif a == 0:
    print('a равно 0')
elif a == 1:   # elif может быть сколько угодно
    print('a равно 1')
else:
    print ('a не равно 5')
print ('======Строка выполняется всегда======')

# это можно описать через словарь с выбором
user_input = int(input('Введите число :'))
d = {5: 'а равно 5', 0: 'а равно 0', 1: 'a равно 1', }
print (d.get(user_input, 'а не равно 0,1,5'))

# проверка наличия чего-то в чём-то
# 10 in {1,2,3,4}
# 10 not in (1,2,3,4)
item = 10
items = [1, 2, 5, 10, 100]
i = item in items 
print (i)
# проверка подстроки в строке
word = 'vlan'
command = 'switchport access vlan 10'
w = word in command
print (w)

if items and type(items) == list:
    print ('В списке есть значения')

# пример с проверкой пароля
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

if len(password) < 8:
    print ('Пароль слишком короткий')
elif username in password:
    print ('Пароль содержит имя пользователя')
else:
    print ('Пароль для пользователя {} установлен'.format(username))

