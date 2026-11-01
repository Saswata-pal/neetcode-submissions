class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sub_box= [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in sub_box[box_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                sub_box[box_idx].add(val)

        return True