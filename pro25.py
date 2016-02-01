#http://www.douban.com/note/233667480/
ab1=[1,1]
#ab11=[1,1]
#ab2=[1,-1]
i=0
n=1
temp=[0,0]
while i<10**999:
    temp[0]=ab1[0]+5*ab1[1]
    temp[1]=ab1[0]+ab1[1]
    ab1[0]=temp[0]
    ab1[1]=temp[1]
    #ab2[0]=ab2[0]-5*ab2[1]
    #ab2[1]=-ab2[0]+ab2[1]
    n=n+1
    i=ab1[1]/(2**(n-1))
print n
