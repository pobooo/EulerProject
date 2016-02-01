below = int(1e3)
sieve = range(2, below)
p = 2
while p < below:
    if sieve[p - 2] > 0:
        no_prime = range(2 * p, below, p)
        for i in no_prime:
            sieve[i - 2] = 0
    p += 1

last_tri_num=3
tri_num=6
index=4
fac_num=2
prime=[2,3]
while fac_num<=500:
    p_fac_num=[0]*len(sieve)
    temp=tri_num
    for j in range(len(sieve)-1):
            if sieve[j]!=0:
                while temp%sieve[j]==0:
                    temp=temp/sieve[j]
                    p_fac_num[j]=p_fac_num[j]+1
    fac_num=1
    for ele in p_fac_num:
            fac_num=fac_num*(ele+1)
    fac_num=fac_num
    last_tri_num=tri_num
    tri_num=tri_num+index
    index=index+1
print last_tri_num
