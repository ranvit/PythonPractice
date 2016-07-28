#! /usr/bin/env python3

steps = 0
def collatz(val):
    global steps
    print(val)
    steps += 1
    if val == 1:
        return
    elif val % 2 == 1:
        return collatz((val*3)+1)
    elif val % 2 == 0:
        return collatz(val//2)


print('Enter a number to start at.')
while True:
    try:
        start = int(input())
        break
    except ValueError:
        print('You must enter an integer.')
collatz(start)
print('Program terminated after ' + str(steps) + ' steps.')
