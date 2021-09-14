# пример генерации конфига
from sys import argv

interface = argv[1]
vlan = argv[2]


access_template = ['switchport mode access', # список строк
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

print ('interface {}'.format(interface))
access = '\n'.join(access_template) # делаем одну строку и к ней format
print(access.format(vlan))


args = ['Gi0/5', '55']
int, vl = args # распаковка списка

print (int,vl)