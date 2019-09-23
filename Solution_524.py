class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # write your code  here
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''