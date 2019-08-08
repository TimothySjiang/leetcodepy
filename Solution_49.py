class Solution:
    def groupAnagrams(self, strs):
        r = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            r[key] = r.get(key, []) + [s]

        return list(r.values())