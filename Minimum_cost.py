def solver(cost,salary,severance,nums):
    dp = {0:0}
    for req in nums:
        tmp = collections.defaultdict(lambda: float('inf'))
        for key in dp:
            if key >= req:
                for i in range(req,key+1):
                    tmp[i] = min(tmp[i],dp[key]+i*salary+(key-i)*severance)
            else:  tmp[req] = min(tmp[req],dp[key]+req*salary+(req-key)*cost)
        dp = tmp
    return min(dp.values())