temp=2**1000
sum=0
while temp!=0:
    sum=sum+temp%10
    temp=temp//10
print sum
