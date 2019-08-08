p = 0
n = int(input())
x = 0
y = 0
i = 1
while i<=n:
    p += 10
    if i%4 == 1:
        x += p
        y = y
        #print(x," ",y)
    elif i%4 == 2:
        x = x
        y += p
        #print(x," ",y)
    elif i%4 == 3:
        x = (x - p)
        y = y
        #print(x," ",y)
    else:
        x = x
        y = (y - p)
        #print(x," ",y)
    i += 1
print("the answer: ",x," ",y)
