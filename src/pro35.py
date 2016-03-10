import math
def primelist(sieveLength):
    finalprime = []
    prime = range(2,sieveLength)
    primeflag = [True]*len(prime)
    maxFactor = int(math.sqrt(sieveLength))
    for i in range(0,maxFactor):
        if primeflag[i]:
            firstPrime = prime[i]
            if firstPrime >= maxFactor:
                break
            for j in range(2,sieveLength//firstPrime):
                temp = j*firstPrime
                primeflag[temp-2] = False
    for i in range(0,len(prime)):
        if primeflag[i]:
            finalprime.append(prime[i])
    return finalprime

prime = primelist(1000000)

