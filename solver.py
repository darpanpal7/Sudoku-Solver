# SODUKO SOLVER
#================================================================================================
""" This is a program that checks if the given input soduko is valid and finds the solution.  """


def isValidSudoku(board) -> bool:

    """ Function that checks if the given soduko is valid or not and return value as 'bool' """

    #checking for each row
    for i in range (9) :
        s = board[i]
        for c in s :
            if s.count(c) > 1 and c != 0 :
                return False
            
    #checking for each column           
    for i in range (9) :
        s = []
        for j in range (9) :
            s.append(board[j][i])
        for c in s :
            if s.count(c) > 1 and c != 0 :
                return False
            
    #checking for each small grid
    for i in range (0,9,3) :
        for j in range (0,9,3) :
            s = []
            p = i+3
            q = j+3
            for k in range(i,p) :
                for l in range(j,q) :
                    s.append(board[k][l])
            for c in s :
                if s.count(c) > 1 and c != 0 :
                    return False
                
    #if all rules are valid, then
    return True


def validNumber(x,y,n,board) -> bool :

    """ Function that checks for given 'x' and 'y',
        if 'n' is a possible entry on board[x][y] """

    #checking for the 'x'th row
    for i in range (9) :
        if board[x][i] == n :
            return False

    #checking for the 'y'th column        
    for i in range (9) :
        if board[i][y] == n :
            return False
        
    #checking for the small grid that contains (x,y)    
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0,3) :
        for j in range (0,3) :
            if board[x0+i][y0+j] == n :
                return False

    #if all rules are valid, then
    return True

def solveSudoku(board) -> None :

    """ Function that solves sudoku and prints one solution """
    
    for i in range (9) :
        for j in range (9) :
            if board[i][j] == 0 :
                for n in range (1,10) :
                    if validNumber(i,j,n,board) :
                        board[i][j] = n
                        solveSudoku(board) #recursive call to solve sudoku further
                        board[i][j] = 0    #if solution fails, backtrack 
                return

    #printing solution
    for i in range (9) :
        print(board[i])
        
    raise SystemExit

if __name__ == "__main__" :
    board = [[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]
    
    if isValidSudoku(board) :
        print("Solution : ")
        solveSudoku(board)
    else :
        print("Sudoku is not valid.")
