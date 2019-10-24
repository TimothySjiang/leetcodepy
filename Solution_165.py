class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        p1 = 0
        p2 = 0
        while p1 < len(version1) and p2 < len(version2):
            v1 = int(version1[p1])
            v2 = int(version2[p2])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            p1 += 1
            p2 += 1
        if p1 < len(version1):
            while p1 < len(version1):
                if int(version1[p1]):
                    return 1
                p1 += 1
            return 0
        if p2 < len(version2):
            while p2 < len(version2):
                if int(version2[p2]):
                    return -1
                p2 += 1
            return 0
        return 0