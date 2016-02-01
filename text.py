f = open("pro18.txt", "r").readlines()
values = []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(token)
    values.append(temp)
#values.reverse()
