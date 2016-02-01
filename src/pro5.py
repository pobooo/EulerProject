sum=0
i1=1
while i1<=100:
    i2=1
    while i2<=100:
        if i1!=i2:
            sum=sum+i1*i2
        i2=i2+1
    i1=i1+1
print sum
