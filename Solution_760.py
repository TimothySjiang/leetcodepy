class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]