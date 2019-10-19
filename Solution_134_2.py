#TLE
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            rest = gas[start] - cost[start]
            if rest >= 0:
                curr = (start + 1) % len(gas)
                while curr != start:
                    rest += gas[curr] - cost[curr]
                    if rest >= 0:
                        curr = (curr + 1) % len(gas)
                    else:
                        break
                if curr == start:
                    return start
        return -1
