import copy


PLAYER_X = "X"
PLAYER_O = "O"


def is_free_to_mark(board, movement): # Board: Matriz Movement: Tupla (x,y)
    x ,y = movement[0], movement[1]
    return board[y][x] is None


def players(board):
    quantity1 = 0
    quantity2 = 0

    for row in board:
        for column in row:
            if(column==PLAYER_X):
                quantity1+=1
            if(column==PLAYER_O):
                quantity2+=1
    if(quantity1==quantity2):
        return PLAYER_X
    else:
        return PLAYER_O
    """
    Returns the player who must move in state s
    """

    raise Exception("Not implemented yet")


def actions(board):
    moves = []
    for row in range(len(board)): 
        for column in range(len(board[row])):
            if board[row][column] is None: 
                moves.append((column, row)) 
    return moves

def result(board, action):
    x,y=action
    moves=actions(board)
    if(action in moves):
        new_board= copy.deepcopy(board)
        new_board[y][x]=players(board)
        return new_board

    """
    Returns the state after taking action a in state s
    """

    raise Exception("Not implemented yet")


def terminal(board):
    moves=actions(board)
    if(moves==[]):
        return True
    for row in board:
        x1=row[0]
        x2=row[1]
        x3=row[2]
        if(x1==PLAYER_X and x2==PLAYER_X and x3==PLAYER_X):
            return True
        elif(x1==PLAYER_O and x2==PLAYER_O and x3==PLAYER_O):
            return True
    for column in range(3):
        y1=board[0][column]
        y2=board[1][column]
        y3=board[2][column]
        if(y1==PLAYER_X and y2==PLAYER_X and y3==PLAYER_X):
            return True
        elif(y1==PLAYER_O and y2==PLAYER_O and y3==PLAYER_O):
            return True
    d1=board[0][0]
    d2=board[1][1]
    d3=board[2][2]
    if(d1==PLAYER_X and d2==PLAYER_X and d3==PLAYER_X):
        return True
    elif(d1==PLAYER_O and d2==PLAYER_O and d3==PLAYER_O):
        return True
    d1=board[0][2]
    d3=board[2][0]
    if(d1==PLAYER_X and d2==PLAYER_X and d3==PLAYER_X):
        return True
    elif(d1==PLAYER_O and d2==PLAYER_O and d3==PLAYER_O):
        return True
    
    return False
    """
    Checks whether state s is a terminal state
    """

    raise Exception("Not implemented yet")


def utility(board):
    for row in board:
        x1=row[0]
        x2=row[1]
        x3=row[2]
        if(x1==PLAYER_X and x2==PLAYER_X and x3==PLAYER_X):
            return 1
        elif(x1==PLAYER_O and x2==PLAYER_O and x3==PLAYER_O):
            return -1
    for column in range(3):
        y1=board[0][column]
        y2=board[1][column]
        y3=board[2][column]
        if(y1==PLAYER_X and y2==PLAYER_X and y3==PLAYER_X):
            return 1
        elif(y1==PLAYER_O and y2==PLAYER_O and y3==PLAYER_O):
            return -1
    d1=board[0][0]
    d2=board[1][1]
    d3=board[2][2]
    if(d1==PLAYER_X and d2==PLAYER_X and d3==PLAYER_X):
        return 1
    elif(d1==PLAYER_O and d2==PLAYER_O and d3==PLAYER_O):
        return -1
    d1=board[0][2]
    d3=board[2][0]
    if(d1==PLAYER_X and d2==PLAYER_X and d3==PLAYER_X):
        return 1
    elif(d1==PLAYER_O and d2==PLAYER_O and d3==PLAYER_O):
        return -1
    
    return 0
            
    """
    Final numeric value for terminal state s
    """
    raise Exception("Not implemented yet")
