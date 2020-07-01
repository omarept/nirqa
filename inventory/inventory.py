import re
from tabulate import tabulate

def extract_version_ios(line):
    version = re.search(r"^Cisco.*, Version (\S+),.*$", line).group(1)
    return version

def extract_uptime_hostname(line):
    uptime = re.search(r".*(\d.+)", line).group(1)
    hostname = re.search(r"^(\S+).*", line).group(1)
    return hostname, uptime

def extract_serial(line):
    serial = re.search(r".*ID (\S+)", line).group(1)
    return serial

def extract_platform(line):
    platform = re.search(r"^cisco (\S+).*", line).group(1)
    return platform


def extract_hostname_nxos(line):
    hostname = re.search(r"^.*Device name: (\S+)", line).group(1)
    return hostname

def extract_platform_nxos(line):
    platform = re.search(r"^Nexus (\S+).*", line).group(1)
    return platform


def process_input_command(file, type_os):
    '''This function read the file and return a list with desired values
    '''
    with open(file) as f:
        show_command = f.read()
        lines_show_command = show_command.split('\n')
    
    device_values = list()
    if type_os == 'ios':
        for line in lines_show_command:
            if 'uptime' in line:
                hostname, uptime = extract_uptime_hostname(line)
            elif 'IOS Software' in line:
                version = extract_version_ios(line)
            elif 'board ID' in line:
                serial = extract_serial(line)
            elif 'bytes of memory' in line:
                platform = extract_platform(line)
        device_values.append(hostname)
        device_values.append(platform)
        device_values.append(version)
        device_values.append(serial)
        device_values.append(uptime)
    elif type_os == 'nxos':
        for line in lines_show_command:
            if 'Device name' in line:
                hostname = extract_hostname_nxos(line)
            elif 'the Nexus Operating System' in line:
                platform = extract_platform_nxos(line)

            
        device_values.append(hostname)
        device_values.append(platform)
        
    return device_values





data = list()

device = process_input_command('r1_show_ver.txt', 'ios')
data.append(device)
device = process_input_command('r2_show_ver.txt', 'ios')
data.append(device)
device = process_input_command('r3_show_ver.txt', 'ios')
data.append(device)
device = process_input_command('nx1_show_ver.txt', 'nxos')
data.append(device)

headers = ['Hostname','Platform', 'OS Version', 'Serial Number', 'Uptime']

print(tabulate(data, headers, tablefmt="simple"))


