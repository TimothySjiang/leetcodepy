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
        celeb = 0

        for i in range(1, n):
            if knows(celeb, i):
                celeb = i

        # Check if the final candicate is the celebrity
        for i in range(n):
            if celeb != i and knows(celeb, i):
                return -1
            if celeb != i and not knows(i, celeb):
                return -1

        return celeb