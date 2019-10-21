#TLE
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        results = []
        self.recursive(s,0,wordSet,[],results)
        return results

    def recursive(self,s,index,wordSet,result,results):
        if index == len(s):
            results.append(' '.join(result))
            return
        for i in range(index,len(s)):
            if s[index:i+1] in wordSet:
                self.recursive(s,i+1,wordSet,result+[s[index:i + 1]],results)