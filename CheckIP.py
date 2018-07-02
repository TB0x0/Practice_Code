'''
Given a string as input, create a program to evaluate whether or not it is a valid IPv4 address.

A valid IP address should be in the form of: a.b.c.d where a, b, c and d are integer values ranging from 0 to 255 inclusive. You MUST have 4 integers in the string. You can’t have a 3 integer IP address or one that’s more than 4

Rules: No imports (excluding required ones)

For example:
127.0.0.1 - valid
127.255.255.255 - valid
257.0.0.1 - invalid
127.0.0.0.1 - invalid
'''

def checkIP():
    address = input('Please input a valid IPv4 address: ')
    address_list = address.split('.')
    if (len(address_list) != 4):
        print('That IP is invalid')
        return 0
    for i in range(0,4):
        print('Checking value ' + str(i+1))
        if (int(address_list[i]) > 255 or int(address_list[i]) < 0):
            print('An out of bounds value was given')
            return 0

    print('IPv4 address is valid.')
