import time
start = time.time()

c = 0
for n in range(1000000, 10000000):
    n = str(n)
    x = ''
    y =[]
    for i in range(0, len(n)):
        if n[i] not in x:
            x += n[i]
            y.append(n.count(n[i]))
    if max(y)<3:
        c += 1
print(c)


end = time.time()
t = end - start
print(t)