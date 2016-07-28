#! usr/bin/python3
# regexStrip.py works like the strip() method by using Regexs

#use match object.start and .end to take substrings of paramStr

import re

def regStrip(paramStr, paramReg = r'\s*'):

    frontReg = re.compile('^(' + paramReg + ')*')
    backReg = re.compile('(' + paramReg + ')*$')

    frontMo = frontReg.search(paramStr)
    backMo = backReg.search(paramStr)

    start = 0
    end = len(paramStr)
    
    if frontMo != None:
        start = frontMo.end()
        
    if backMo != None:
        end = backMo.start()
        
    print('Stripping...')
    newStr = paramStr[start:end]
    print(newStr)
    return newStr

while True:
    print('\nType the original string first, or EXIT to terminate')
    text = input()
    if text == 'EXIT':
        print('Terminating...')
        break

    print('''Type the substring that needs to be stripped
Or [ENTER] to strip whitespace''')
    
    strip = input()
    if strip == '':
        regStrip(text)
    else:
        regStrip(text, strip)
