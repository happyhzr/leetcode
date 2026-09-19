from main import Solution


def test_lemonadeChange():
    s = Solution()
    assert s.lemonadeChange([5, 5, 5, 10, 20]) == True
    assert s.lemonadeChange([5, 5, 10, 10, 20]) == False
    assert s.lemonadeChange([5, 5, 5, 5, 10, 20, 5, 5, 5, 5]) == True
