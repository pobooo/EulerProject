import prolib
leftTruncatablePrime = [2,3,5,7]
count =0
while count <= 11:
    for i in leftTruncatablePrime:
        for j in [2,3,5,7]:
            newPrime = prolib.rPlusDigits(i,j)
            temp = newPrime
            while len(str(temp)) >= 2:
                if len(str(temp)) > 2:
                    if isPrime(temp):
                        temp = prolib.lTruncation(temp)
                    else:
                        break
                else:
                    if isPrime(temp):
                        count += 1
                        leftTruncatablePrime.append(newprime)
print leftTruncatablePrime
                        
                    
