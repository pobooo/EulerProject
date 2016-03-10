import time
start=time.clock()
target = 200
coinSet = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]*(target+1)
ways[0]=1
for coin in coinSet:
    for change in range(coin,target+1):
        ways[change] += ways[change-coin]
print time.clock()-start
print ways[target]

