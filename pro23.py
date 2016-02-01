def sum_of_divisors(x):
    sum=0
    for i in range(1,x//2+1):
        if x%i==0:
            sum=sum+i
    return sum
def ab_num():
    ab_all=[]
    for i in range(12,28123):
        if sum_of_divisors(i)>i:
            ab_all.extend([i])
    return ab_all
flag=[True]*28123
ab=ab_num()
for i in ab:
    for j in ab:
        s=i+j
        if s<=28123:
            if flag[s-1]:
                flag[s-1]=False
sum=0
for i in range(28123):
    if flag[i]:
        sum=sum+i+1
print sum
