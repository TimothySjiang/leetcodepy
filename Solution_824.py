class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set(['a','e','i','o','u'])
        S = S.split()
        res = []
        for i,word in enumerate(S):
            if word[0].lower() in vowel:
                res.append(word+'ma'+'a'*(i+1))
            else:
                res.append(word[1:]+word[0]+'ma'+'a'*(i+1))
        return ' '.join(res)