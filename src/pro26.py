squencelength=0
for i in range(999,1,-1):
    if squencelength >= i:
        break
    findReminder = [0]*i
    value = 1
    position=0
    while findReminder[value] == 0 and value != 0:
        findReminder[value] = position
        value *= 10
        value %= i
        print value
        position += 1
    if position - findReminder[value] >= squencelength:
        squencelength = position - findReminder[value]
print i+1


