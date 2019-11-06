import collections
def mostCommon(arr):
    counter = collections.Counter(arr)
    res = []
    maxFreq = float('-inf')
    for k in counter:
        if counter[k] > maxFreq:
            res = [k]
            maxFreq = counter[k]
        elif counter[k] == maxFreq:
            res.append(k)

    return res



if __name__ == '__main__':
    print(mostCommon([2,2,3,3,5]))
