interface = input ('Введите тип и номер интерфейса: ') # на ввод попадает строка
vlan = input ('Введите номер VLAN: ')

access_template = ['switchport mode access', # список строк
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

print ('interface {}'.format(interface))
access = '\n'.join(access_template) # делаем одну строку и к ней format
print(access.format(vlan))



input ('Для продолжения нажмите Enter') # это для остановки скрипта, что бы посмотреть результат
