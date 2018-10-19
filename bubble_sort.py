def myBubbleSort(theList):
    the_list=theList.copy()
    L = len(the_list) - 1
    
    for n in range(L):
        for i in range(L - n):
            if the_list[i] > the_list[i + 1]:
                the_list[i],the_list[i + 1] = the_list[i + 1],the_list[i]
                
    return the_list
