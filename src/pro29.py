import time
squence = []
for a in range(2,101):
    for b in range(2,101):
        temp = a**b
        if temp not in squence:
            squence.append(temp)
print len(squence)
