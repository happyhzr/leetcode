class Solution:
    def candy(self, ratings: list[int]) -> int:
        candy_list = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i], candy_list[i + 1] + 1)
        return sum(candy_list)
