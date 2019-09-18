class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        count = 0
        while True:
            for ch in 'balloon':
                if c[ch] > 0:
                    c[ch] -= 1
                else:
                    return count
            count += 1