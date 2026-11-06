class Solution:
    def isValidSudoku(self,board):
        # ROW CHECK
        for i in range(0,9):
            chk_row = {}
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] not in chk_row:
                        chk_row[board[i][j]] = 1
                        # print(f"{i},{j} = {chk_row}")
                    else:
                        chk_row[board[i][j]] += 1
                        # print(f"The row false is triggered at {i},{j}")
                        # print(f"{i},{j} = {chk_row}")
                        return False
        # print("------------------------------------------------")
        # COLUMN CHECK
        for j in range(0,9):
            chk_col = {}
            for i in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] not in chk_col:
                        chk_col[board[i][j]] = 1
                        # print(f"{i},{j} = {chk_col}")
                    else:
                        chk_col[board[i][j]] += 1
                        # print(f"The col false is triggered at {i},{j}")
                        # print(f"{i},{j} = {chk_col}")
                        return False
        # print("------------------------------------------------")
        # SQUARES CHECK
        for i in range(0,8,3):
            for j in range(0,8,3):
                chk_sqr = {}
                for m in range(0,3):
                    for n in range(0,3):
                        if board[i+m][j+n] != ".":
                            if board[i+m][j+n] not in chk_sqr:
                                chk_sqr[board[i+m][j+n]] = 1
                                # print(f"{i},{j}//{m},{n} = {chk_sqr}")
                            else:
                                chk_sqr[board[i+m][j+n]] += 1
                                # print(f"The sqr false is triggered at {i},{j} square")
                                # print(f"{i+m},{j+n} = {chk_sqr}")
                                return False                      
        return True