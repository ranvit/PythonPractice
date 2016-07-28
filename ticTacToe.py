theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#printBoard(theBoard)

turns = ['X', 'O']
boolean = 0
for i in range(9):
    printBoard(theBoard)
    print(turns[boolean] + '\'s move')
    move = input()
    theBoard[move] = turns[boolean]
    boolean = (boolean+1)%2

printBoard(theBoard)
    
