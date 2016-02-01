def factorial(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
thenum=range(10)
theone=[]
sum=0
num_of_rest=range(9)
num_of_rest.reverse()
while sum<=1000000:
    for i in range(len(thenum)):
        j=0
        while sum<=1000000:
            sum=sum+num_of_rest[i]
            if sum>=1000000:
                break
            j=j+1
        theone.append(thenum[j])
        del thenum[j]
