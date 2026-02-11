from main import Solution


def test_repeatedSubstringPattern():
    s = Solution()
    assert s.repeatedSubstringPattern("abab") == True
    assert s.repeatedSubstringPattern("aba") == False
    assert s.repeatedSubstringPattern("abcabcabcabc") == True
