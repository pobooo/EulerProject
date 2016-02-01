def prime(x):
    i=2
    flag=True
    while i<x:
        if x%i==0:
            flag=False
            break
        i=i+1
    return flag

i1=0
z=2
while i1<10001:
    if prime(z):
        i1=i1+1
    z=z+1
print z-1,i1
