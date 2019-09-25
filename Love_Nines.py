class Solution:
    def loveNine(self,N):
        count = 0
        while N > 0:
            N -= 9
            count += 1
            if not N % 10:
                break
        return count if N >= 0 else -1

def main():
    s = Solution()
    print(s.loveNine(209))
    print(s.loveNine(37))
    print(s.loveNine(20))
    print(s.loveNine(9))

if __name__ == '__main__':
    main()