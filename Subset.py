def generateSubset(set):
    if (len(set) == 0):
        b = [[]]
        return b
    else:
        allSubsets = generateSubset(set[1:])
       # moreSubsets = []

        moreSubsets = [];

        for subset in allSubsets:
            newSubset = subset.copy()
            subset.append(set[0])
            moreSubsets.append(newSubset)
            moreSubsets.append(subset)

        return moreSubsets


if (__name__ == '__main__'):
    a = "dinesh"
    print(a[len(a) - 1])
    inp = [int(x) for x in input().split()]
    answer = generateSubset(inp)
    print(answer)
    print(len(answer) == 2**len(inp));