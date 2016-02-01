def sum_of_divisors(x):
    sum=0
    for i in range(1,x//2+1):
        if x%i==0:
            sum=sum+i
    return sum
an=[2]*9999
for i in range(9999):
    if an[i]==2:
        last_temp=i+1
        temp=sum_of_divisors(last_temp)
        new_temp=sum_of_divisors(temp)
        if last_temp==temp:
            an[last_temp-1]=False
        else:
            if last_temp==new_temp:
                an[last_temp-1]=True
                if temp<9999:
                    an[temp-1]=True
        while last_temp!=new_temp:
            an[last_temp-1]=False
            if temp>=9999:
                break
            last_temp=temp
            temp=new_temp
            new_temp=sum_of_divisors(temp)
            if last_temp==temp:
                an[last_temp-1]=False
            else:
                if last_temp==new_temp:
                    an[last_temp-1]=True
                    if temp<9999:
                        an[temp-1]=True
                    else:
                        break
            
xsum=0        
for i in range(len(an)):
    if an[i]:
        xsum=xsum+i+1
print xsum
print sum_of_divisors(220)
print sum_of_divisors(284)
