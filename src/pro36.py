def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True
def d2b(n):
    List = []
    while n//2 != 0 or n == 1:
        List.append(n%2)
        n = n//2
    return List
def isPalindromic(n):
    List = d2b(n)
    for i in range(0,len(List)//2):
        if List[i] != List[len(List)-i-1]:
            return False
    return True

primaryNum = []
for k in range(1,1000):
    primaryNum.append(int(str(k)+str(k)[::-1]))
for k in range(1,10):
    primaryNum.append(k)
for k in range(1,100):
    for j in range(1,10):
        primaryNum.append(int(str(k)+str(j)+str(k)[::-1]))

Num = list(primaryNum)
for i in primaryNum:
    if i%2 == 0:
        Num.remove(i)
    else:
        if not isPalindromic(i):
            Num.remove(i)
print Num
print sum(Num)
                
