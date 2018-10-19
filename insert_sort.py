def myInsertSort(theList):
    
    newList = []
    newList.append(theList[0])
    
    for i in theList[1:]:
        
        if i <= newList[0]:
            newList.insert(0,i)
        elif i >= newList[-1]:
            newList.append(i)
        else:
            l = len(newList)
            
            for j in range(l):
                
                if newList[j] <= i and i <= newList[j + 1]:
                    newList.insert(j + 1,i)
                    break

                
    return newList

print(myInsertSort([5,4,3,2,1]))
