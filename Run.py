import checking
import insert_sort
import shell_sort
import bubble_sort
import time

    

times=10
size=5000
frist=1
last=300

for i in range(times):
    print('times=%d'%(i+1))
    theList = checking.randintList(size,frist,last)

    start = time.time()
    newList = insert_sort.myInsertSort(theList)
    end = time.time()
    spend = end - start
    print('insert,{:.4}'.format(spend))
    
    start = time.time()
    newList = shell_sort.myShell(theList)
    end = time.time()
    spend = end - start
    print('shell,{:.4}'.format(spend))
    
    start = time.time()
    newList = bubble_sort.myBubbleSort(theList)
    end = time.time()
    spend = end - start
    print('bubble,{:.4}'.format(spend))
