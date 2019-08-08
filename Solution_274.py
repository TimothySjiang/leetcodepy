class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i

        return len(citations)