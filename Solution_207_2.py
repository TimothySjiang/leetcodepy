class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Pre = collections.defaultdict(set)
        Need = collections.defaultdict(set)

        for edge in prerequisites:
            Need[edge[0]].add(edge[1])
            Pre[edge[1]].add(edge[0])

        leaves = []
        for k in range(numCourses):
            if k not in Need:
                leaves.append(k)

        while leaves:
            for i in range(len(leaves)):
                leaf = leaves.pop()
                neighbors = Pre[leaf]
                for course in neighbors:
                    Need[course].remove(leaf)
                    if not Need[course]:
                        leaves.append(course)

        for k in range(numCourses):
            if Need[k]:
                return False
        return True
