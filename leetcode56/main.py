#!/usr/bin/env python3


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key=lambda interval: interval.start)
        result = []
        for val in intervals:
            if result:
                last = result[-1]
                if last.end >= val.start:
                    if val.end > last.end:
                        last.end = val.end
                else:
                    result.append(val)
            else:
                result.append(val)
        return result


if __name__ == '__main__':
    lst = [[1, 3], [2, 6], [8, 10], [15, 18], ]
    intervals = []
    for val in lst:
        intervals.append(Interval(val[0], val[1]))
    s = Solution()
    result = s.merge(intervals)
    for val in result:
        print(val.start, val.end)
