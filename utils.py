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
    row=0
    moves=[]
    for row_list in board:
        row+=1
        for column in enumerate(row_list):
            if(board[column][row]==None):
                moves+=[(column,row)]
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
    return moves==[]
    """
    Checks whether state s is a terminal state
    """

    raise Exception("Not implemented yet")


def utility(board):
    """
    Final numeric value for terminal state s
    """

    raise Exception("Not implemented yet")
