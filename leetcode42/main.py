#!/usr/bin/env python


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        size = len(height)
        max_left = [0] * size
        max_right = [0] * size
        max_left[0] = height[0]
        max_right[size - 1] = height[size - 1]

        for i in range(1, size):
            max_left[i] = max(max_left[i - 1], height[i])

        for i in reversed(range(0, size - 1)):
            max_right[i] = max(max_right[i + 1], height[i])

        ans = 0
        for i in range(0, size):
            ans += min(max_left[i], max_right[i]) - height[i]

        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
