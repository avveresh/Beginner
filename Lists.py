# l1 = [1,2,3,4] это список, изменяемый тип
# a = 'line1' line1 это коробочка на которую ссылается переменная - а
# a = 4, 'line1' уже забыта, без метки и она удаляется из памяти, теперь переменная а ссылается на коробочку со значением - 4
list1 = [1,2,66] # изменяемый тип, изменяется на месте, id не меняется
list1.insert(2,250)
list1.remove(1)
list1.append(555)
list2 = sorted(list1) # не меняет list1
print (list1, list1[2])
print (list2)
vlans = ['1', '2', '3', '60'] # список строк, с числами не работает
vlans_str = ','.join(vlans) # делаем одну строку
print (vlans_str)