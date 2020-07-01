from tabulate import tabulate

headers = ['Hostname','Platform', 'OS Version', 'Serial Number', 'Uptime']
data = [['R1','CSR1000V', '16.6.8', '9ELWT7FOM78','8 minutes' ], 
        ['R2','CSR1000V','16.6.8','9LDWBQC6DYC','12 minutes'],
        ['R3','CSR1000V','16.6.8','9IWA86M4B72','15 minutes'],
        ['NX1','Nexus9000','7.0(3)I7(4)','9QNOBLD0840','17 minute(s)']]

print(tabulate(data, headers, tablefmt="grid"))