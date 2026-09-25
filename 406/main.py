class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=self.cmp)
        queue = []
        for person in people:
            position = person[1]
            queue.insert(position, person)
        return queue

    def cmp(self, x):
        return -x[0], x[1]
