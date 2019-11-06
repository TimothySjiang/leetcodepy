#Quora OA
def maxRibbon(arr,k):
    l = 0
    r = max(arr) + 1
    while l < r:
        mid = l + (r-l)//2
        if isValid(mid,arr,k):
            l = mid + 1
        else:
            r = mid
    return l - 1

def isValid(mid,arr,k):
    if k <= sum([x//mid for x in arr]):
        return True
    return False

if __name__ == '__main__':
    print(maxRibbon([1,2,3,4,9],5))
