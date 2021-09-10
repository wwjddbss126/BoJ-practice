# https://www.acmicpc.net/problem/8958
import sys
n = int(sys.stdin.readline())
testlist = [sys.stdin.readline().strip() for i in range(n)]
testscore = []
for i in range(n):
    score = 0
    add = 1
    for j in range(len(testlist[i])):
        if(testlist[i][j] == 'O'):
            if(j!=0 and testlist[i][j-1] == 'O'):
                add += 1
            if(j!=0 and testlist[i][j-1] == 'X'):
                add = 1
            score += add
    testscore.append(score)
for k in range(len(testscore)):
    print(testscore[k], end='\n')
