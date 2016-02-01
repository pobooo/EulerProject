# -*- coding: cp936 -*-
#埃拉托斯特尼筛法
'''
sum=(1+2000000)*1000000
p=range(2,2000001)
i=p[0]
while i**2<2000000:
    j=2
    del p[0]
    while i*j<=2000000:
        if i*j in p:
            sum=sum-i*j
            p.remove(i*j)
        j=j+1
    i=p[0]
print sum-1
'''
is_prime=[True]*(2000000-1)
for i in range(2,1414):
    if is_prime[i-2]:
        j=i*i
        while j<=2000000:
            is_prime[j-2]=False
            j=j+i
prime=range(2,2000001)
i=0
sum=0
while i<=2000000-2:
    if is_prime[i]:
        sum=sum+prime[i]
    i=i+1
print sum
    
