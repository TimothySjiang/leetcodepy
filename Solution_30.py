class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        dic = collections.Counter(words)
        wlength = len(words[0])
        res = []
        for i in range(wlength):
            window = collections.Counter()
            count = 0
            for j in range(i, len(s), wlength):
                word = s[j:j + wlength]
                if word in dic:
                    window[word] += 1
                    count += 1
                    while window[word] > dic[word]:
                        pos = j - wlength * (count - 1)
                        rword = s[pos:pos + wlength]
                        window[rword] -= 1
                        count -= 1
                else:
                    window = collections.Counter()
                    count = 0
                if count == len(words):
                    res.append(j - wlength * (count - 1))

        return res