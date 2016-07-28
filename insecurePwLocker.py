#! /usr/bin/env python3

# An insecure password locker which copies the chosen account's password into
# the system clipboard for easy pasting

import sys, pyperclip

PASSWORDS = {
    'email': 'emailPassword',
    'facebook': 'facebookPassword',
    'amazon': 'amazonPassword'
}

if len(sys.argv) != 2:
    print('Usage: python insecurePwLocker.py [account]')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + "'s password has been copied to the clipboard")

else:
    print("'" + account + '\' isn\'t stored. Exiting')
