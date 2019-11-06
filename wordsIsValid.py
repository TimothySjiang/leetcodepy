#Quora OA
def wordsIsValid(words,letters):
    validSet = set(letters)
    count = 0
    for word in words:
        isValid = True
        for ch in word:
            if 'a' <= ch.lower() <= 'z' and not ch.lower() in validSet:
                isValid = False
                break
        count += isValid

    return count


if __name__ == '__main__':
    print(wordsIsValid(['hEllo##', 'This^^'],['h', 'e', 'l', 'o', 't', 'h', 's']))

