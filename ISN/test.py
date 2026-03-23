t1 = []
n = 2
l = []
for i in range(n):
    for j in range(n):
        l.append(i*j)
    t1.append(l)
t1[0][1]=5
print(t1)
