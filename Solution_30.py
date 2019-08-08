class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        hash = collections.Counter(words)
        res = []
        wlength = len(words[0])

        for start in range(0, wlength):
            slidingWindow = collections.Counter()
            wCount = 0
            for i in range(start, len(s), wlength):
                word = s[i: i + wlength]
                if word in hash:
                    slidingWindow[word] += 1
                    wCount += 1

                    while hash[word] < slidingWindow[word]:
                        pos = i - wlength * (wCount - 1)
                        removeWord = s[pos: pos + wlength]
                        slidingWindow[removeWord] -= 1
                        wCount -= 1
                else:
                    slidingWindow.clear()
                    wCount = 0
                if wCount == len(words):
                    res.append(i - wlength * (wCount - 1))

        return res