class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1  :
            return 0
        res = 0
        dp = [0 for i in range(len(s))]    	#初始化
        for i in range(len(s) - 2, -1, -1) :
            if s[i] == '(' :		#如果s[i] = '('，则需要找到右括号和它匹配
                j = i + dp[i + 1] + 1
                if j < len(s) and s[j] == ')' :	#如果没越界且为右括号，那么有dp[i] = dp[i + 1] + 2
                    dp[i] = dp[i + 1] + 2
                    if j + 1 < len(s):			#还要将j + 1开头的子串加进来
                        dp[i] += dp[j + 1]
                res = max(res, dp[i])
        return res