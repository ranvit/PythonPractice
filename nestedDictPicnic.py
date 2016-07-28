import pprint
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}
prettyDict = {}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

itemList = ['apples', 'cups', 'cake', 'ham sandwiches', 'pretzels', 'apple pies']
itemList.sort()

for i in itemList:
    #print(i + ': ' + str(totalBrought(allGuests, i))) #similar output to pprint
    prettyDict[i] = totalBrought(allGuests, i)

pprint.pprint(prettyDict)
