import math
def primelist(sieveLength):##generate Primes smaller than sieveLength
    finalprime = []
    prime = range(2,sieveLength)
    primeflag = [True]*len(prime)
    maxFactor = int(math.sqrt(sieveLength+1))
    for i in range(0,maxFactor):
        if primeflag[i]:
            firstPrime = prime[i]
            if firstPrime > maxFactor:
                break
            for j in range(2,sieveLength//firstPrime+1):
                temp = j*firstPrime
                if temp-2 <= sieveLength - 3:
                    primeflag[temp-2] = False
    for i in range(0,len(prime)):
        if primeflag[i]:
            finalprime.append(prime[i])
    print primeflag
    return finalprime

def lshift(n):
    l = list(str(n))[1:]
    l.append(str(n)[0])
    return int("".join(l))

def lTruncation(n):
    l = list(str(n))[1:]
    return int("".join(l))

def rTruncation(n):
    l = list(str(n))[:-1]
    return int("".join(l))

def rPlusDigits(i,j):
    return int(str(i)+str(j))

def isPrime(n):
    prime = primelist(n+1)
    if prime[-1] == n:
        return True
    else:
        return False
