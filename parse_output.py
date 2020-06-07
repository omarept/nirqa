import re

with open('r3_lldp.txt') as f:
        output = f.read()

list_output = output.split('\n')

list_output_no_blanks = list(filter(None,list_output))

semaphore = 0

for item in list_output_no_blanks:
    match_item = re.match('^Device', item)
    if match_item:
        list_formatted = []
        semaphore = 1
    elif semaphore == 1 :
        list_formatted.append(item)
print(list_formatted[:-1])