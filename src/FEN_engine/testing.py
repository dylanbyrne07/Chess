from create_fen import *
from parseFen import *

if __name__ == '__main__':
    Board = parse_FEN(eg3)
    FEN = create_FEM(Board)

    for row in Board:
        print(row)
    
    print(FEN)