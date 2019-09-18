class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        preNum = [0] * numCourses
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            preNum[prerequisites[i][0]] += 1

        for i in range(numCourses):
            avaiableCourse = False
            for j in range(numCourses):
                if preNum[j] == 0:
                    for k in graph[j]:
                        preNum[k] -= 1
                    avaiableCourse = True
                    preNum[j] = -1
                    break
            if not avaiableCourse:
                return False
        return True