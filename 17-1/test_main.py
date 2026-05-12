from main import Solution


def test_main() -> None:
    s = Solution()
    assert s.letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert s.letterCombinations("2") == ["a", "b", "c"]
