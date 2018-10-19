def myBubbleSort(theList):

    j = len(theList) - 1
    
    for n in range(j):
        
        for i in range(j - n):
            
            if theList[i] > theList[i + 1]:
                theList[i],theList[i + 1] = theList[i + 1],theList[i]
                
    return theList

