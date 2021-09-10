a = {'Name' : 'Alexander', 'Surename' : 'Vereshchetin', 'Age' : '42'} # это словарь: ключ - значение
a.setdefault('address')
b = list(a.keys()) # словарь -> список
c = list(a)
c1 = list(a.values())
c2 = list(a.items())
print (a['Name'], a.values(), a.keys(),a.items(),b)
print (c)
print (c1)
print (c2)
