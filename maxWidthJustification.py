tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def widthCount(tableData):
    colWidth = [0] * len(tableData)
    for i in range(len(tableData)):
        for x in range(len(tableData[i])):
            curWidth = len(tableData[i][x])
            if curWidth > colWidth[i]:
                colWidth[i] = curWidth

    return colWidth

outp = widthCount(tableData)
#print(outp)

def printTable(tableData, colWidth):
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidth[y]), end='')
            if y < 2: print(' ', end='')
        print()

printTable(tableData, outp)
