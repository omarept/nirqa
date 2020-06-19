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
    print("---")
    print("Getting Token")
    print("---")


print("Getting Attached Devices")

uuid_device = '005dd83e-5c3f-92b7-bd78-56e5c63e44d8'

device_url = 'https://192.168.66.11/dataservice/template/config/running/' + uuid_device

response = session.get(url=device_url, verify=False)
response = json.loads(response.content)

print(response['config'])

