class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=self.cmp)
        arrows = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                arrows += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])
        return arrows

    def cmp(self, x: list[int]):
        return x[0]
