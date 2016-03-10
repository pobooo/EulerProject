def isPandigital(a,b):
    string = str(a)+str(b)+str(a*b)
    if len(string) != 9:
        return False
    for i in range(1,10):
        if str(i) not in string:
            return False
    return True

pandigital = []
for a in range(1,98):
    for b in range (123,6789):
        c = a*b
        if isPandigital(a,b) and c not in pandigital:
            pandigital.append(c)
print sum(pandigital)
    
        
