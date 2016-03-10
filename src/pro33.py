def isNontrivalfraction(a,b):
    stringa = str(a)
    stringb = str(b)
    if a == b or '0' in stringa or '0' in stringb or stringa[0] == stringa[1] or stringb[1] == stringb[0] or len(stringa) != 2 or len(stringb) !=2:
        return False
    else:
        for i in stringa:
            for j in stringb:
                if i == j:
                    temp1 = stringa.replace(i,'')
                    temp2 = stringb.replace(i,'')
                    if int(temp1)*b == int(temp2)*a:
                        return True
        return False

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b, a%b
    return a

frac = []
for i in range(11,99):
    for j in range(i,99):
        if isNontrivalfraction(i,j):
            frac.append([i,j])
print frac
sum1 = 1
sum2 = 1
for i in frac:
    sum1 *= i[0]
    sum2 *= i[1]
print sum2/gcd(sum1,sum2)
