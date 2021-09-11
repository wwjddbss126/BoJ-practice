# https://www.acmicpc.net/problem/4673
num = set(range(1,10001))
self = set()
for i in range(1, 10001):
    self.add(sum([int(x) for x in str(i)]) + i)
num = num.difference(self)
for j in range(len(num)):
    print(sorted(num)[j], end='\n')
