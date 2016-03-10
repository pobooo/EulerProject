sumall = 0 
for i in range(2,354294):
    sum = 0
    temp = i
    while (temp//10 != 0 or (temp//10 ==0 and temp%10!=0)):
        sum += (temp%10)**5
        temp = temp//10
    if i == sum:
        sumall += i
        print i
print sumall
