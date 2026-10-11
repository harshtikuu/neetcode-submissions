class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_nums(nums: List[str]) -> bool:
            seen = set()
            for char in nums:
                if char != '.'  and char in seen:
                    return False
                seen.add(char)
            return True
        
        for row in board:
            if not valid_nums(row):
                return False
        
        for j in range(9):
            col = []
            for i in range(9):
               col.append((board[i][j]))
            if not valid_nums(col):
                return False

        for x in range(0,9,3):
            for y in range(0,9,3):
                nums = []
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        nums.append(board[i][j])
                if not valid_nums(nums):
                    return False
        return True