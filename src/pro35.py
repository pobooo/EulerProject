import math
def primelist(sieveLength):
    finalprime = []
    prime = range(2,sieveLength-1)
    primeflag = [True]*len(prime)
    maxFactor = int(math.sqrt(sieveLength))
    for i in range(0,maxFactor+1):
        if primeflag[i]:
            firstPrime = prime[i]
            if firstPrime >= maxFactor:
                break
            for j in range(2,sieveLength//firstPrime+1):
                temp = j*firstPrime
                if temp-2 <= sieveLength - 3:
                    primeflag[temp-2] = False
    for i in range(0,len(prime)):
        if primeflag[i]:
            finalprime.append(prime[i])
    return finalprime

def shift(n):
    l = list(str(n))[1:]
    l.append(str(n)[0])
    return int("".join(l))

prime = primelist(1000000)
Circularflag = [True]*len(prime)
for i in range(0,len(prime)):
    for j in str(prime[i]):
        if int(j)%2 == 0 or int(j)%5 == 0:
            Circularflag[i] = False
            break
circular = [2,5]
for i in range(0,len(prime)):
    if Circularflag[i]:
        circular.append(prime[i])
##circular = [23435,421, 12,3435, 21,546]
finalcircular = list(circular)
for i in circular:
    temp = i
    ##print i
    for j in range(0,len(str(i))+6):
        temp = shift(temp)
        if int(temp) not in finalcircular and i in finalcircular:
           ##print 11111
            finalcircular.remove(i)
print len(finalcircular)
print finalcircular
        
