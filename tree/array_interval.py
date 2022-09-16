# 这个里面主要是关于用interval组成的数组相关的算法
# interval是 [start, end]这样的　start < end

def findLongestChain(pairs: List[List[int]]) -> int:
    '''
        function:
            对于一个interval的数组，找出能够形成最长数对链的长度，(a, b), (c, d)能形成链，必须b < c
        date:
            2022-09-22
        Args:
            pairs interval数组
        Return:
            最长数对链的长度
        Comments:
            如果我用interval的start进行排序然后进行贪心，那么会出问题[1, 10], [2, 3], [3, 5]; 如果使用interval的end进行排序然后贪心，那么可以的，我后来发现我之前用的是dp的方法dp[i] = dp[i - 1]　然后一个for循环 for j in range(i - 1, 0, -1): 如果找到一个pairs[i - 1][0] > pairs[j - 1][1]的话，那么dp[i] = max(dp[i], dp[j] + 1)之后break
    '''
    pairs.sort(key = lambda x : x[1])
    last = None
    ans = 0
    for start, end in pairs:
        # 这里有个非常严重的问题 not last 当last为0的时候就也会通过
        #if not last or start > last:
        if last is None or start > last: # correct
            last = end
            ans += 1
    return ans
