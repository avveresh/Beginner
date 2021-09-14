import sys
print (sys.argv)

vlan = sys.argv[1]
print (vlan)

access_template = ['switchport mode access', # список строк
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

access = '\n'.join(access_template) # делаем одну строку и к ней format
print(access.format(vlan))