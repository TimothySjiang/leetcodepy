class Solution:
    def countArrangement(self, N: int) -> int:
        def backtrack(num, index):
            if not num % index or not index % num:
                if index == 1:
                    nonlocal count
                    count += 1
                else:
                    for i in range(1, N + 1):
                        if i not in visited:
                            visited.add(i)
                            backtrack(i, index - 1)
                            visited.remove(i)

        count = 0
        visited = set()
        for i in range(1, N + 1):
            visited.add(i)
            backtrack(i, N)
            visited.remove(i)

        return count