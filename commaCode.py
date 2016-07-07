strList = ['apples', 'bananas', 'tofu', 'cats']
intList = [1, 2, 3, 4]
mixList = ['apples', 2, 'tofu', 4, 'pie', 6]
arrayList = [strList, intList, mixList]

print(arrayList[0][1])

def commafunc(param):
    spam2 = ''
    length = len(param)
    for i in range(length):
        
        spam2 += str(param[i])
        
        if i == length-1 :
            spam2 += '.'
            continue
        
        if i == length-2 :
            spam2 += ' and '
            continue
        
        spam2 += ', '

    print(spam2)
    print()

while True:
    print('Enter 1 for strList, 2 for intList, 3 for mixList, 0 to exit')
    act = int(input())
    if act < 4 and act > 0:
        commafunc(arrayList[act-1])
    elif act == 0:
        print('Exiting..')
        break
    else:
        print(str(act) + ' is not a valid input.')

"""
Can be done using spam2 = [] and then By using ''.join

list1 = ['1', '2', '3']
str1 = ''.join(list1)

Or if the list is of integers, convert the elements before joining them.
list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)
"""
