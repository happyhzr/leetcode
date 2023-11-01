class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        loop = numRows * 2 - 2
        each_col = len(s) // loop
        n_col = each_col * (numRows - 1)
        if 0 <= len(s) % loop and len(s) % loop <= numRows - 1:
            n_col += 1
        else:
            n_col += len(s) % loop - numRows + 2
        matrix = [[col] * n_col for col in [""] * numRows]
        i = 0
        j = 0
        for k, c in enumerate(s):
            matrix[i][j] = c
            if k % loop >= 0 and k % loop <= numRows - 2:
                i += 1
            elif k % loop >= numRows - 1:
                i -= 1
                j += 1
        result = ""
        for row in matrix:
            row_str = "".join(row)
            result += row_str
        return result
