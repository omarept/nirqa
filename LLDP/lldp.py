import re
from netmiko import Netmiko
from tabulate import tabulate



def get_output(device_id, send_command):
    '''This function connect to a device run
        a command and return the output
    '''
    net_conn = Netmiko(**device_id)
    output = net_conn.send_command(send_command)
    return output


def get_lldp_neighbors(input_cmd):
    '''This function receive the output command
        and return the relevant information.
    '''
    parser = input_cmd.split('\n')
    parser_no_blanks = list(filter(None, parser))
    lldp_neighbors_no_headers = parser_no_blanks[4:len(parser_no_blanks)-1]
    return lldp_neighbors_no_headers

def get_hostname(input_cmd):
    parser = input_cmd.split()
    return parser[1]


def neighbors_routers( lldp_preformatted ):
    router_neighbors = []
    for line in lldp_preformatted:
        tmp = line.split()
        del tmp[2:4]
        router_neighbors = router_neighbors + [tmp]
    return router_neighbors

def print_output(dyct_input):
    
    headers = ["Hostname", "Local Interface", "Neighbor", "Neighbor Interface"]
    table=list()


    for k,v in dyct_output.items():
        info = v
        table.append(info)
    
    print()

    return





###---- main -----


with open('LLDP/devices.txt') as f:
    devices = f.read()
    list_devices = devices.split()

dyct={}
dyct_output={}

for item in list_devices:
    match_hostname = re.match('^\[.*\]$', item)
    if match_hostname:
        if len(dyct) != 0:
            r = get_output(dyct, 'show lldp neig')
            h = get_output(dyct,'show run | inc hostname')
            lldp_neighbors = get_lldp_neighbors(r)
            hostname = get_hostname(h)
            dyct_output[hostname] = neighbors_routers(lldp_neighbors)
        dyct={}
    else:
        (k,v)=item.split(':')
        dyct[k] = v
    
r = get_output(dyct, 'show lldp neig')
h = get_output(dyct, 'show run | inc hostname')
lldp_neighbors = get_lldp_neighbors(r)
hostname = get_hostname(h)
dyct_output[hostname] = neighbors_routers(lldp_neighbors)

print(dyct_output)

print_output(dyct_output)