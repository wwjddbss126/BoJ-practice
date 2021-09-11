# https://www.acmicpc.net/problem/1157
a = input().upper()
abc = list(range(65, 91))
cnt = [0] * 26
mx = []

for i in range(len(a)):
    cnt[abc.index(ord(a[i]))] += 1

mxidx = max(cnt)
for i in range(26):
    if(mxidx <= cnt[i]):
        mx.append(cnt[i])
        mxidx = cnt[i]

if(len(mx) != 1):
    print("?")
else:
    print(chr(abc[cnt.index(mx[0])]))
