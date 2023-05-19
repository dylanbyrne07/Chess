def create_FEM(board):
    FEN = ""
    Last_one_is_space = False
    count = 0

    for row in board:
        for col_index, col in enumerate(row):
            if col != ' ':

                if Last_one_is_space == True:
                    FEN += str(count)

                FEN += col

                Last_one_is_space = False
                count = 0
            elif col == ' ':
                if Last_one_is_space == False:
                    count = 1
                
                elif Last_one_is_space == True:
                    count +=1

                Last_one_is_space = True
                

        Last_one_is_space = False
        if count > 0:
            FEN += str(count)

        if row != board[-1]:
            FEN += '/'
        
    return FEN


