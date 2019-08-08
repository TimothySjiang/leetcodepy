class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A or not B or not C or not D:
            return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()

        visited = set()

        self.ans = 0
        if A[0] + B[0] + C[0] + D[0] <= 0 and (len(A), len(B), len(C), len(D)) not in visited:
            visited.add((len(A), len(B), len(C), len(D)))
            if A[0] + B[0] + C[0] + D[0] == 0:
                self.ans += 1

            self.walk(A[1:], B, C, D, visited)
            self.walk(A, B[1:], C, D, visited)
            self.walk(A, B, C[1:], D, visited)
            self.walk(A, B, C, D[1:], visited)

        return self.ans

    def walk(self, A, B, C, D, visited):
        if A and B and C and D:
            if A[0] + B[0] + C[0] + D[0] <= 0 and (len(A), len(B), len(C), len(D)) not in visited:
                visited.add((len(A), len(B), len(C), len(D)))

                if A[0] + B[0] + C[0] + D[0] == 0:
                    self.ans += 1

                self.walk(A[1:], B, C, D, visited)
                self.walk(A, B[1:], C, D, visited)
                self.walk(A, B, C[1:], D, visited)
                self.walk(A, B, C, D[1:], visited)           