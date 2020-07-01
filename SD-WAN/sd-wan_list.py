import requests
import sys
import json
from tabulate import tabulate

requests.packages.urllib3.disable_warnings()

sdwan_url = 'https://192.168.66.11/j_security_check'
sdwan_credentials = {'j_username':'admin', 'j_password':'admin'}

session = requests.session()
response = session.post(url=sdwan_url, data=sdwan_credentials, verify=False)

if b'<html>' in response.content:
	print(f"Login Failed, {response.status_code}")
	exit(0)
else:
    print(f"Login Success, {response.status_code}")


print("Getting Inventory...")

device_url = 'https://192.168.66.11/dataservice/device'

response = session.get(url=device_url, verify=False)
response = json.loads(response.content)


headers = ["Host Name", "Reachability", "Status", "Device IP", "Site-ID", "Host Type", "Version"]
table = list()


for device in response['data']:
    info = [device['host-name'], device['reachability'], device['status'], device['deviceId'], 
    device['site-id'], device['device-model'], device['version']]
    table.append(info)

print(tabulate(table, headers, tablefmt="grid"))


