last_tri_num=3
tri_num=6
index=4
fac_num=2
prime=[2,3]
temp=0
is_prime=[True]*len(prime)
while fac_num<=500:
    p=range(last_tri_num+1,tri_num+1)
    prime.extend(p)
    p1=[True]*len(p)
    is_prime.extend(p1)
    for i in prime:
        if i*i<=tri_num:
            j=i*i
            while j<=tri_num:
                is_prime[j-2]=False             
                j=j+i
    p_fac_num=[0]*len(prime)
    temp=tri_num
    for j in range(len(prime)-1):
            if is_prime[j]:
                while temp%prime[j]==0:
                    temp=temp/prime[j]
                    p_fac_num[j]=p_fac_num[j]+1
    fac_num=1
    for ele in p_fac_num:
            fac_num=fac_num*(ele+1)
    fac_num=fac_num
    last_tri_num=tri_num
    tri_num=tri_num+index
    index=index+1
print last_tri_num
