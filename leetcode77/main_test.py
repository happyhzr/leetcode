#!/usr/bin/env python3

import unittest
import random

from main import Solution


class CombineTest(unittest.TestCase):
    def test(self):
        n = random.randint(0, 16)
        k = random.randint(0, n)
        print('n', n, 'k', k)
        s = Solution()
        result = s.combine(n, k)
        self.assertEqual(len(result), CombineTest.cnk(n, k))
        for array in result:
            self.assertFalse(CombineTest.is_number_repeated(array))
        for i in range(len(result)):
            for j in range(i):
                self.assertNotEqual(set(result[i]), set(result[j]))

    @staticmethod
    def is_number_repeated(array):
        mark = {}
        for value in array:
            if value in mark.keys():
                return True
            mark[value] = True
        return False

    @staticmethod
    def cnk(n, k):
        result = 1
        for i in range(k + 1, n + 1):
            result = result * i
        for i in range(1, n - k + 1):
            result = result // i
        return result


if __name__ == '__main__':
    unittest.main()
