from main import Solution


def test_main() -> None:
    so = Solution()
    s = "PAYPALISHIRING"
    num_rows = 3
    assert so.convert(s, num_rows) == "PAHNAPLSIIGYIR"
    s = "PAYPALISHIRING"
    num_rows = 4
    assert so.convert(s, num_rows) == "PINALSIGYAHRPI"
    s="A"
    num_rows=1
    assert so.convert(s, num_rows) == "A"
