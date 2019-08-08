class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def o(w):
            return [order.find(w) for w in w]

        def compare(w1, w2):

            try:
                for i in range(len(w1)):
                    if w1[i] < w2[i]:
                        return True
                    elif w1[i] == w2[i]:
                        continue
                    else:
                        return False
            except:
                return (len(w1) < len(w2))

        for i in range(len(words) - 1):
            if compare(o(words[i]), o(words[i + 1])):
                continue
            else:
                return False

        return True
