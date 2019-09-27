class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float('inf')
        for i in range(len(arr)-1):
            diff = min(diff,arr[i+1]-arr[i])
        results = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == diff:
                results.append([arr[i],arr[i+1]])
        return results