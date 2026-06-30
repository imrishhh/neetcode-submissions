class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val)
                idx = (i // 3) * 3 + j // 3
                if val in sub[idx]:
                    return False
                sub[idx].add(val)
        return True