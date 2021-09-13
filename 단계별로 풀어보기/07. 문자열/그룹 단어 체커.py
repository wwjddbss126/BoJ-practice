# https://www.acmicpc.net/problem/1316
word = [input() for x in range(int(input()))]
grp = 0
for i in word:
    cnt = [0] * 26
    idx = -1
    for j in range(len(i)):
        if(idx != (ord(i[j]) - 97)):
            idx = (ord(i[j])) - 97
            cnt[idx] += 1       
    if(max(cnt)==1):
        grp += 1
print(grp)
