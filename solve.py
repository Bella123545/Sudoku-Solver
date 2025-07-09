
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(board, num, pos):
    #check if num isn't in the row
    for i in range(len(board[0])):
        if board[pos[0]][i]==num and pos[1]!=i:
            return False
    #check if num isn't in the column
    for i in range(len(board[0])):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False
        
    #check if num ins't in the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    #if num is not in row, column or box return true
    return True

def printBoard(board):
    for i in range(len(board)):
        #every three 3 split up the board with ----
        if i%3 and i!=0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board)):
            if j%3==0 and j!=0:
                print("|", end="")
            if j==8:
                print(board[i][j])
            else:print(str(board[i][j]+" ",end=""))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j) #the row, column