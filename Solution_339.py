import functools

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        result, depth = 0, 1
        while (nestedList):
            result += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = functools.reduce(lambda: x,y:x + y, [x.getList() for x in nestedList if not x.isInteger()])
            depth += 1

        return result
