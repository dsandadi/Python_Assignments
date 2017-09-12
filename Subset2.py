def getSubsets2(set):
    allSubsets = []
    totalWords = 2**len(set)
    for i in range(0,totalWords):
        allSubsets.append(generateSubsets(set,i))
    return allSubsets

def generateSubsets(set, pos):
    index = 0
    allSubsets = []

    while pos > 0:
        if(pos&1 == 1):
            allSubsets.append(set[index])
        pos >>= 1
        index = index + 1

    return allSubsets

if(__name__ == '__main__'):
    feed = list(int(x) for x in input().split())
    print(getSubsets2(feed))