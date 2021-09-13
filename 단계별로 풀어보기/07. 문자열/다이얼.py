# https://www.acmicpc.net/problem/5622
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = 0
inputlist = [x for x in input()]
for i in range(len(inputlist)):
    for j in range(len(dial)):
        if(inputlist[i] in dial[j]):
            sec += j + 3
print(sec)
