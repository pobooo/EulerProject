prox=1
for i in range(2,101):
    prox=prox*i
sum=0
string=str(prox)
for i in string:
    sum=sum+int(i)
print sum
