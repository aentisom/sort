import insert_sort


def shellList(the_list):#希尔增量
    shell_list = []
    N = len(the_list)
    
    while N != 1:
        N = int(N/2)
        shell_list.append(N)
        
    return shell_list

def myShell(the_list):#希尔排序
    
    gap_list=shellList(the_list)
    L=len(the_list)
    
    for gap in gap_list:
        if gap == 1:
            return insert_sort.myInsertSort(the_list)
        flag = 0#flag是分组的序号
        
        for i in range(gap):
            list_temp = []
            
            while flag < L:#提取分组
                list_temp.append(the_list[flag])
                flag += gap
                
            insert_list = insert_sort.myInsertSort(list_temp)#inser_list变量,insert_sort模块,排序分组
            k = -1
            flag -= gap
            
            while flag >= 0:#使用新分组替换原列表对应元素
                the_list[flag] = insert_list[k]#k是insert_list专用索引
                k -= 1
                flag -= gap
                
            flag = i + 1

