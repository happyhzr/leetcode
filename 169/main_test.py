import unittest
from typing import List
import random

from main import Solution


class TestSolution(unittest.TestCase):
    def test_majorityElement(self):
        nums = self.newNums()
        print(nums)
        s = Solution()
        got = s.majorityElement(nums)
        count = 0
        for v in nums:
            if v == got:
                count += 1
        self.assertTrue(count > len(nums) // 2)

    def newNums(self) -> List[int]:
        n = random.randrange(1024)
        majar_length = random.randrange(n // 2 + 1, n + 1)
        majar_n = random.randrange(1024)
        nums = []
        for _ in range(majar_length):
            nums.append(majar_n)
        for _ in range(n - majar_length):
            nums.append(random.randrange(1024))
        random.shuffle(nums)
        return nums


if __name__ == "__main__":
    unittest.main()
