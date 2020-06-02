from __future__ import print_function, unicode_literals




#with open("r2_lldp.txt") as f:
#    lldp_neighbors = f.readlines()

# parsing the file 
# removing header and tail
# lldp_neighbors_no_headers = lldp_neighbors[6:len(lldp_neighbors)-3]

#print(lldp_neighbors)


def get_lldp_neighbors(input_file):
    with open(input_file) as f:
        lldp_neighbors = f.readlines()
    hostname =  lldp_neighbors[0].partition('#')
    lldp_neighbors_no_headers = lldp_neighbors[6:len(lldp_neighbors)-3]
    return lldp_neighbors_no_headers, hostname[0]

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
    


dyct_output = {}

lldp_neighbors1, hostname1 = get_lldp_neighbors('r1_lldp.txt')
lldp_neighbors2, hostname2 = get_lldp_neighbors('r2_lldp.txt')
lldp_neighbors3, hostname3 = get_lldp_neighbors('r3_lldp.txt')
lldp_neighbors4, hostname4 = get_lldp_neighbors('r4_lldp.txt')



dyct_output[hostname1] = neighbors_routers(lldp_neighbors1)
dyct_output[hostname2] = neighbors_routers(lldp_neighbors2)
dyct_output[hostname3] = neighbors_routers(lldp_neighbors3)
dyct_output[hostname4] = neighbors_routers(lldp_neighbors4)


print_output(dyct_output)





    

    



