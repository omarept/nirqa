d = {}
with open("r2_credentials.txt") as f:
    for line in f:
        (key, val) = line.split(':')
        d[key] = val[:-1]

print (d)