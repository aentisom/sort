def myInsertSort(theList):
    newList = []
    newList.append(theList[0])
    
    for i in theList[1:]:
        if i >= newList[-1]:
            newList.append(i)
        elif i <= newList[0]:
            newList.insert(0,i)
        else:
            L = len(newList)
            
            for flag in range(L):
                if newList[flag] <= i and i <= newList[flag + 1]:
                    newList.insert(flag + 1,i)
                    break

    return newList
