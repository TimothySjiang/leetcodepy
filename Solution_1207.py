class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = collections.Counter(arr)
        count = set()
        for k in occur:
            if occur[k] in count:
                return False
            else:
                count.add(occur[k])
        return True