# https://www.acmicpc.net/problem/2675
import sys
T = int(sys.stdin.readline())
case = [sys.stdin.readline().strip().split(' ') for x in range(T)]
P = []
for i in range(T):
    tmp = ''
    for j in range(len(case[i][1])):
        for k in range(int(case[i][0])):
            tmp += case[i][1][j]
    P.append(tmp)
for i in range(T):
    print(P[i])
