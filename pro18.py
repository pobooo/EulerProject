# -*- coding: cp936 -*-
import time
tStart = time.time()
path=[[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
#path=[[3],[7,4],[2,4,6],[8,5,9,3]]
path_val=[0]*len(path)
last_path_val=[0]*len(path)
last_path_val[0]=path[0][0]
#path_patten=path
'''
for i in range(len(path_patten)):
    for j in range(len(path_patten[i])):
        path_patten[i][j]=0
'''
for i in range(1,len(path)):
    path_val[0]=last_path_val[0]+path[i][0]
    path_val[i]=last_path_val[i-1]+path[i][i]
    for j in range(1,i):
            val1=last_path_val[j-1]+path[i][j]
            val2=last_path_val[j]+path[i][j]
            if val1<val2:
                path_val[j]=val2
                #path_patten[i-1][j]=1
            else:
                path_val[j]=val1
                #path_patten[i-1][j-1]=1
    last_path_val=path_val
    path_val=[0]*len(path)#�������ʹ��� ��֪Ϊʲô
print max(last_path_val)
print "Run Time = " + str(time.time() - tStart)
