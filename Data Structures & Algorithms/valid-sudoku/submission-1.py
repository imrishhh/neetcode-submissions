class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = len(board)
        rows = [0] * board_len
        cols = [0] * board_len
        sub = [0] * board_len
        for i in range(0, board_len):
            for j in range(0, board_len):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j])
                pos = 1 << (val - 1)
                if rows[i] & pos > 0:
                    return False
                rows[i] |= pos
                if cols[j] & pos > 0:
                    return False
                cols[j] |= pos
                idx = (i // 3) * 3 + j // 3
                if sub[idx] & pos > 0:
                    return False
                sub[idx] |= pos
        return True