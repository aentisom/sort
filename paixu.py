def mymin(a):#找最小
    Min=a[0]
    j=0
    for i in range(len(a)):
        if Min>a[i]:
            Min=a[i]
            j=i
    return [Min,j]
def paixu(a):#排序
    new=[]
    lista=a.copy()
    while len(lista)!=0:
        b=mymin(lista)
        new.append(b[0])
        del lista[b[1]]
    return new
def shell_list(a):#求希尔增量
    shell_list=[]
    N=len(a)
    while N!=1:
        N=int(N/2)
        shell_list.append(N)
    return shell_list

def xiao_paopao(a):#最后的排序
    j=len(a)
    for i in range(j-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return a
def myshell(a):#希尔排序
    gap=shell_list(a)
    L=len(a)
    b=a.copy()
    #print('gap',gap)
    for gap_ in gap:
        if gap_!=1:
            M=0
            for i in range(gap_):
                list_temp=[]
                while M<L:
                    list_temp.append(b[M])
                    M+=gap_
                #print('list_temp',list_temp)
                cha_list=paixu(list_temp)
                #print('cha_list',cha_list)
                k=-1
                M-=gap_
                while M>=0:
                    
                    b[M]=cha_list[k]
                    k-=1
                    M-=gap_
                    #print('M',M,'len',len(b),'b',b,'k',k)
                M=i+1
        else:
            xiao_paopao(b)
    return b


'''
e=[7,6,5,4,3,2,1,5,3,99,342,235,66,2,0,0,4,32,5]
print(myshell(e))
'''
