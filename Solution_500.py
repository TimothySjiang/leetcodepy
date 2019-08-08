class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for w in words:
            for j in range(3):
                if w[0].lower() in line[j]:
                    flag = 1
                    for i in w:
                        if i.lower() not in line[j]:
                            flag = 0
                    if flag == 1:
                        res.append(w)
        return res