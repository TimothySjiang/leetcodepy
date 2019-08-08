class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        S = '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
        return S