from main import Solution


def test_isValid():
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("([])") == True
    assert s.isValid("([)]") == False
