def myBubbleSort(theList):

    L = len(theList) - 1
    
    for n in range(L):
        
        for i in range(L - n):
            
            if theList[i] > theList[i + 1]:
                theList[i],theList[i + 1] = theList[i + 1],theList[i]
                
    return theList
