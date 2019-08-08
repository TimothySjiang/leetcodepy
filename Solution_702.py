class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        hi = 1
        while reader.get(hi) < target: hi <<= 1
        lo = hi >> 1
        while lo <= hi:
            mid = lo + hi >> 1
            if reader.get(mid) < target: lo = mid + 1
            elif reader.get(mid) > target: hi = mid - 1
            else: return mid
        return -1