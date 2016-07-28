#! /usr/bin/env python3

# Determines if the param string is a phone number or not.
# Without regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
#        print('Incorrect length')
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
#            print('A phone number needs numbers')
            return False

    if text[3] != '-':
#        print('Incorrect formatting')
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
#            print('A phone number needs numbers')
            return False

    if text[7] != '-':
#        print('Incorrect formatting')
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
#            print('A phone number needs numbers')
            return False

    return True
"""
print('Enter a phone number [xxx-xxx-xxxx]')

while True:
    text = input()
    if isPhoneNumber(text):
        print('Deteced a phone number in required format')
        break
    else:
        print("Input wasn't a phone number.")
        print('Try again in [xxx-xxx-xxxx] format')
"""

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
#    print(chunk)
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
