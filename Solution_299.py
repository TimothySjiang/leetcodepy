class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        table = collections.defaultdict(int)
        bull, cow = 0, 0

        for index, s in enumerate(secret):
            if guess[index] == s:
                bull += 1
            else:
                table[s] += 1

        for index, s in enumerate(guess):
            if (s != secret[index]) and table[s]:
                cow += 1
                table[s] -= 1

        return str(bull) + "A" + str(cow) + "B"