#! usr/bin/python3
# regexPassword.py detects passowrd strength

import re

passRegex = []

passRegex1 = re.compile(r'''(
    ([a-z])+
    ([A-Z])+
    ([0-9])+
)''', re.VERBOSE)

passRegex2 = re.compile(r'''(
    ([a-z])+
    ([0-9])+
    ([A-Z])+
)''', re.VERBOSE)

passRegex3 = re.compile(r'''(
    ([A-Z])+
    ([a-z])+
    ([0-9])+
)''', re.VERBOSE)

passRegex4 = re.compile(r'''(
    ([A-Z])+
    ([0-9])+
    ([a-z])+
)''', re.VERBOSE)

passRegex5 = re.compile(r'''(
    ([0-9])+
    ([A-Z])+
    ([a-z])+
)''', re.VERBOSE)

passRegex6 = re.compile(r'''(
    ([0-9])+
    ([a-z])+
    ([A-Z])+
)''', re.VERBOSE)

passRegex.append(passRegex1)
passRegex.append(passRegex2)
passRegex.append(passRegex3)
passRegex.append(passRegex4)
passRegex.append(passRegex5)
passRegex.append(passRegex6)

def regCheck(paramReg, paramPass):
    if paramReg.search(paramPass) != None:
        return True
    return False

def passValid(paramReg, paramPass):
    if len(paramPass) < 8:
        print('Password needs to be 8 characters long')
        return True
    
    for i in range(6):
        if regCheck(paramReg[i], paramPass):
            print('Password is long AND strong ;)')
            return False

    print('Password is long, but not strong :(')
    return True

print('''Enter a password that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.''')
password = input()
while passValid(passRegex, password):
    print('Try again')
    password = input()
print('Exiting...')
