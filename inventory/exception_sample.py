my_dict = {}
#print("Before")
#my_dict['ip_address']
#print("what is my IP address")


try:
    print("Statement Before")
    #my_dict['ip_address']
    print("Statement after")
except KeyError:
    print("Caught Exception")

print("After exception...")