# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = -1
        for i in range(n):
            flag = True
            for j in range(n):
                if knows(i, j) and j != i:
                    flag = False
                    break

            if flag and celebrity >= 0:
                return -1
            if flag:
                celebrity = i

        if celebrity < 0:
            return -1

        for i in range(n):
            if not knows(i, celebrity) and i != celebrity:
                return -1

        return celebrity