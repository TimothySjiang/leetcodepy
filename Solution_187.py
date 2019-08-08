class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s)):
            ten = s[i:i + 10]
            if (ten in seen):
                repeated.add(ten)
            seen.add(ten)

        return list(repeated)
