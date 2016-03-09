import math
sieveLength = 1000
prime = range(2,sieveLength)
maxFactor = int(math.sqrt(sieveLength))
nomPrimeIndex = [0]*sieveLength
for i in range(0,maxFactor):
    firstPrime = prime[i]
    if firstPrime >= maxFactor:
        break
    for j in range(2,sieveLength//firstPrime):
        temp = j*firstPrime
        if temp in prime:
            prime.remove(temp)
aList = range(1,999,2) 
aList.extend(range(-999,-1,2))
bList = map(lambda x,y:x-y,[0]*len(prime),prime)
bList.extend(prime)
maxa=0
maxb=0
maxn=0
for a in aList:
    for b in bList:
        n = 0
        while n*n+a*n+b in prime:
            n += 1
        if n-1 >= maxn:
            maxa = a
            maxb = b
            maxn = n-1
print maxa*maxb
