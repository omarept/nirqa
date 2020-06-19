# script for router connection
from netmiko import Netmiko
from getpass import getpass

'''
router1 = {
    'host': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_xe'
}
'''

def read_variables(file_input):
    router = {}
    with open(file_input) as f:
        for line in f:
            (k, v) = line.split(':')
            router[k] = v[:-1]
    return router

'''
router1 = {}
with open("devices.txt") as f:
    for line in f:
        (key, val) = line.split(':')
        router1[key] = val[:-1]

router2 = {
    'host': '10.1.2.2',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_xe'
}

router3 = {
    'host': '10.1.3.3',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_xe'
}

nx1 = {
    'host': '10.1.4.4',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_nxos'
}
'''

router1 = read_variables('r1_credentials.txt')
router2 = read_variables('r2_credentials.txt')
router3 = read_variables('r3_credentials.txt')
nx1 = read_variables('nx1_credentials.txt')



def get_output(device_id, send_command):
    net_conn = Netmiko(**device_id)
    output = net_conn.send_command(send_command)
    return output


r1 = get_output(router1,'show lldp neig')
print(r1)



'''
r2 = get_output(router2,'show lldp neig')
print(r2)

r3 = get_output(router3,'show lldp neig')
print(r3)

r4 = get_output(nx1,'show lldp neig')
print(r4)
'''
