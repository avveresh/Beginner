# при переприсваивании значений строке, ID будет разным
# конкатенация
# '' - строка, не изменяемый тип данных
a = '123abc  '
b = '456def'
c = a + b
d = '\t\tinterface\r\n'
e = 'I want to go to trip'
years = 'i am {} years old'
c1 = a[1]
c2 =c.upper() # метод upper//у объекта вызвать метод
c3 = type(c)
c4 = d.strip() # удаляет символы справа и слева
c5 = e.split() # из строки делает список элеиентов
c6 = years.format('42') # подстановка в шаблон
print (c,c1,c2,c3,d,c4,c5,c6)
# a =+ 1