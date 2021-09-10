# https://www.acmicpc.net/problem/4344
import sys
n = int(sys.stdin.readline())
score = [sys.stdin.readline().strip().split(' ') for i in range(n)]
avg = []
rat = []

for i in range(n):
    scoresum = 0
    num = int(score[i][0])
    for j in range(1, num+1):
        scoresum += int(score[i][j])
    avg.append(scoresum//num)

for i in range(n):
    cnt = 0
    num = int(score[i][0])
    for j in range(1, num+1):
        if(int(score[i][j])>avg[i]):
            cnt += 1
    rat.append((cnt/num)*100)

for i in range(n):
    res = str('{:.3f}'.format(rat[i])) + "%"
    print(res, end='\n')
