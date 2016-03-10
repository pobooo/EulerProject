def factorial(n):
    if n == 0:
        return 1
    return  n*factorial(n-1)

def isfactorialSum(n):
    string = str(n)
    sum = 0
    for i in string:
        sum += factorial(int(i))
    if sum == n:
        return True
    else:
        return False

sum = 0
for i in range(3,2540160):
    if isfactorialSum(i):
        sum += i
print 

