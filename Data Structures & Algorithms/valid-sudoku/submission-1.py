from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                row_key = i
                col_key = j
                box_key = (i//3, j//3)

                if board[i][j] in row_set[row_key] or board[i][j] in col_set[col_key] or board[i][j] in box_set[box_key]:
                    return False

                row_set[row_key].add(board[i][j])
                col_set[col_key].add(board[i][j])
                box_set[box_key].add(board[i][j])
        return True



