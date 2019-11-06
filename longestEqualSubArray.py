def longestEqualSubArray(arr):
    if not arr: return 0
    if not arr[0]: arr[0] = -1
    res = float('-inf')
    pos = {arr[0]:0,0:-1}
    for i in range(1,len(arr)):
        if not arr[i]:
            arr[i] = arr[i-1] - 1
        else:
            arr[i] = arr[i-1] + 1

        if arr[i] not in pos:
            pos[arr[i]] = i
        else:
            res = max(res,i-pos[arr[i]])
    return res

if __name__ == '__main__':
    print(longestEqualSubArray([0,1,0,1,0,1,1,0,0,1,1,1,1,1]))