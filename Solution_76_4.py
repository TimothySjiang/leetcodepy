class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal = collections.Counter(t)
        formed = len(goal)
        l = r = 0
        window = collections.defaultdict(int)
        ans = (float('inf'), l, r)
        while formed and r < len(s):
            window[s[r]] += 1
            if window[s[r]] == goal[s[r]]:
                formed -= 1
                if not formed:
                    while window[s[l]] > goal[s[l]]:
                        window[s[l]] -= 1
                        l += 1
                    ans = min(ans, (r - l + 1, l, r))
                    window[s[l]] -= 1
                    l += 1
                    formed += 1
            r += 1

        return s[ans[1]:ans[2] + 1] if ans[0] < float('inf') else ''
