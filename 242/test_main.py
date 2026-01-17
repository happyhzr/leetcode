from main import Solution


def test_isAnagram():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
