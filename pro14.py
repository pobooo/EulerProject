nums=range(1,1000000)
for i in range(len(nums)):
    chain_len=0
    if nums[i]!=0:
        temp=nums[i]
        while temp!=1:
            if temp%2==0:
                chain_len=chain_len+1
                temp=temp/2
            else:
                temp=temp*3+1
                chain_len=chain_len+1
            if temp<1000000:
                nums[temp-1]=0
        nums[i]=chain_len
mm=max(nums)
print nums.index(mm)+1
