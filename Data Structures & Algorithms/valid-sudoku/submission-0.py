class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = len(board)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subMat = [set() for _ in range(9)]

        for i in range(0, board_len):
            for j in range(0, board_len):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val)

                idx = (i // 3) * 3 + j // 3

                if val in subMat[idx]:
                    return False
                subMat[idx].add(val)
        return True