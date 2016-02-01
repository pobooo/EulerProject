a=1
b=1
c=1000-2
while a<=500:
    b=1
    while b<=500:
        c=1000-a-b
        t=a*a+b*b
        if t==c*c:
            print a*b*c
            break
        b=b+1
    a=a+1
