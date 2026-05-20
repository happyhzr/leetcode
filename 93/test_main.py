from main import Solution


def test_restoreIpAddresses():
    s = Solution()
    assert s.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"]
    assert s.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert s.restoreIpAddresses("101023") == [
        "1.0.10.23",
        "1.0.102.3",
        "10.1.0.23",
        "10.10.2.3",
        "101.0.2.3",
    ]
