class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word

        self.check()

        self.height = len(self.board)
        self.width = len(board[0])
        self.visited = []
        for i in range(self.height):
            self.visited.append([False]*self.width)

        for i in range(self.height):
            for j in range(self.width):
                if self.dfs(i, j, 0):
                    return True
        return False

    def check(self):
        if self.word == '':
            return True
        height = len(self.board)
        if height == 0:
            return False

    def isInBoundary(self, i, j):
        if 0 <= i and i <= self.height-1 and 0 <= j and j <= self.width-1:
            return True
        return False

    def dfs(self, i, j, k):
        if k == len(self.word):
            return True
        if not self.isInBoundary(i, j):
            return False
        if self.board[i][j] != self.word[k]:
            return False
        if self.visited[i][j] == True:
            return False
        self.visited[i][j] = True
        move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        for index in range(4):
            next_i = i+move[index][0]
            next_j = j+move[index][1]
            if self.dfs(next_i, next_j, k+1):
                return True
        self.visited[i][j] = False
        return False


if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    ans = s.exist(board, 'ABCCED')
    print(ans)
    ans = s.exist(board, 'SEE')
    print(ans)
    ans = s.exist(board, 'ABCB')
    print(ans)
