#! /usr/bin/env python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#TODO: bulletting
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
"""
for i in lines:
    i = '* ' + i
    print(i)
"""

text = '\n'.join(lines)

print(text)
pyperclip.copy(text)
print('Bulletted list has been copied')
