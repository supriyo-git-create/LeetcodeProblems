class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row, return original string
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for char in s:
            rows[curRow] += char
            # Change direction at the top or bottom row
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)
