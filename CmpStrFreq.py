import collections
def cmpStrFreq(str1,str2):
    h1 = collections.Counter(str1)
    h2 = collections.Counter(str2)
    if h1.keys()!= h2.keys():
        return False
    freq1 = collections.Counter(h1.values())
    freq2 = collections.Counter(h2.values())
    if freq1 != freq2:
        return False
    return True


if __name__ == '__main__':
    print(cmpStrFreq('babzcc','abbzczz'))
