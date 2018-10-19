def myInsertSort(theList):
    
    newList = []
    newList.append(theList[0])
    
    for i in theList[1:]:

        if i >= newList[-1]:
            newList.append(i)
        elif i <= newList[0]:
            newList.insert(0,i)
        else:
            l = len(newList)
            
            for j in range(l):
                
                if newList[j] <= i and i <= newList[j + 1]:
                    newList.insert(j + 1,i)
                    break

    return newList
