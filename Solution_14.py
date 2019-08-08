class Solution:
    def longestCommonPrefix(self,strs):
        if((not strs) | (len(strs) == 0)):
            return("")
        shortest = min(strs,key=len)
        for i in range(len(shortest)):
            for other in strs:
                if ((other[i] !=shortest[i])):
                    return shortest[:i]
        return(shortest)  