class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = collections.Counter(s)
        odd = False
        for i in c:
            if c[i] % 2:
                if odd:
                    return False
                else:
                    odd = True
        return True