from random import randint


def randintList(size,start,end):
    newList = []
    for i in range(size):
        newList.append(randint(start,end))
    return newList

def examine(theList):
    for i in range(len(theList)-1):
        if theList[i] > theList[i+1]:
            return False
    return True
