def myInsertSort(theList):
    
    newList = []
    newList.append(theList[0])
    
    for i in theList[1:]:
        
        if i <= newList[0]:
            newList.insert(0,i)
        elif i >= newList[-1]:
            newList.append(i)
        else:
            L = len(newList)
            
            for j in range(L):
                
                if newList[j] <= i and i <= newList[j + 1]:
                    newList.insert(j + 1,i)
                    break

                
    return newList
