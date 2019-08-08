class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def f(n):
            return n%2
        return sorted(A,key=f)