from __future__ import print_function, unicode_literals
from netmiko import Netmiko



def read_variables(file_input):
    router = {}
    with open(file_input) as f:
        for line in f:
            (k, v) = line.split(':')
            router[k] = v[:-1]
    return router



def get_lldp_neighbors(input_cmd):
    #    hostname =  lldp_neighbors[0].partition('#')
    parser = input_cmd.split('\n')
    lldp_neighbors_no_headers = parser[5:len(parser)-3]
    return lldp_neighbors_no_headers

'''
def get_hostname( lldp_output ):
    hostname =  lldp_neighbors[0].partition('#')
    return hostname[0]
'''


def neighbors_routers( lldp_preformatted ):
    router_neighbors = []
    for line in lldp_preformatted:
        tmp = line.split()
        del tmp[2:4]
        router_neighbors = router_neighbors + [tmp]
    return router_neighbors


def print_output(dyct_input):
    
    print('-'*80)
    print("{:^20}{:^20}{:^20}{:^20}".format("Hostname", "Local Interface", "Neighbor", "Neighbor Interface"))
    print('-'*80)
    for k,v in dyct_output.items():
        i=0
        while i <  len(v):
            print("{:^20}{:^20}{:^20}{:^20}".format(k, v[i][1], v[i][0], v[i][2]))
            i = i+1 
    print('-'*80)
    return

router1 = read_variables('r1_credentials.txt')
router2 = read_variables('r2_credentials.txt')
router3 = read_variables('r3_credentials.txt')
nexus1 = read_variables('nx1_credentials.txt')


def get_output(device_id, send_command):
    net_conn = Netmiko(**device_id)
    output = net_conn.send_command(send_command)
    return output


r1 = get_output(router1,'show lldp neig')
r2 = get_output(router2,'show lldp neig')
r3 = get_output(router3,'show lldp neig')
nx1 = get_output(nexus1,'show lldp neig')


dyct_output = {}

lldp_neighbors1 = get_lldp_neighbors(r1)
lldp_neighbors2 = get_lldp_neighbors(r2)
lldp_neighbors3 = get_lldp_neighbors(r3)
lldp_neighbors4 = get_lldp_neighbors(nx1)


dyct_output['R1'] = neighbors_routers(lldp_neighbors1)
dyct_output['R2'] = neighbors_routers(lldp_neighbors2)
dyct_output['R3'] = neighbors_routers(lldp_neighbors3)
dyct_output['NX1'] = neighbors_routers(lldp_neighbors4)

print_output(dyct_output)
