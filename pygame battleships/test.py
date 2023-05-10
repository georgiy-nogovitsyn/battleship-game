import time

t = time.time()
ms = time.time()*1000.0

print(t)
print(ms)

for x in range(10000):
    x ** x

t_new = time.time()
ms_new = time.time()*1000.0

print(t_new - t)
print(ms_new - ms)