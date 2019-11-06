#Quora OA
import collections
def goodTuples(arr):
    if len(arr) < 3:
        return 0
    count = 0
    window = collections.Counter(arr[:3])
    if len(window) == 2:
        count += 1
    for i in range(1,len(arr)-2):
        window[arr[i-1]] -= 1
        if not window[arr[i-1]]:
            del window[arr[i-1]]
        window[arr[i+2]] += 1
        if len(window) == 2:
            count += 1

    return count

if __name__ == '__main__':
    print(goodTuples([1,1,2,1,4,3,2,3]))