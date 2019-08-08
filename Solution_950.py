class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = [i for i in range(N)]
        ans = [None] * N

        for card in sorted(deck):
            ans[index.pop(0)] = card
            if index:
                index.append(index.pop(0))

        return ans