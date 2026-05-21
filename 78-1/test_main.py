from main import Solution


def test_subsets():
    s = Solution()
    assert is_same_set(
        s.subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert is_same_set(s.subsets([0]), [[], [0]])


def is_same_set(s1: list[list[int]], s2: list[list[int]]) -> bool:
    for v1 in s1:
        if v1 not in s2:
            return False
    for v2 in s2:

        if v2 not in s1:
            return False
    return True
