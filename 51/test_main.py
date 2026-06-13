from main import Solution


def test_solveNQueens():
    s = Solution()
    assert s.solveNQueens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert s.solveNQueens(1) == [["Q"]]
