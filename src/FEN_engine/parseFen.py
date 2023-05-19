eg = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
eg2 = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR'
eg3 = '8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8'

def parse_FEN(FEN):
    board = []
    for x in FEN.split('/'):
        line = []
        for y in x:
            if y.isdigit():
                for z in range(int(y)):
                    line.append(' ')
            else:
                line.append(y)
        board.append(line)
    return board
