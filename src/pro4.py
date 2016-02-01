def palindrome(num):
    a=str(num)
    flag=True
    if len(a)%2!=0:
        l=(len(a)-1)/2
    else:
        l=len(a)/2
    for i in range(l):
        if a[i]!=a[len(a)-i-1]:
            flag= False
            break
    return flag

i1=999
i2=999
prod=0
while i1>100:
    i2=999
    while i2>100:
        temp1=i1*i2
        i2=i2-1
        if palindrome(temp1)and prod<=temp1:
           prod=temp1
    i1=i1-1
    
print prod
print i1
print i2
print temp1
