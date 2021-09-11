# https://www.acmicpc.net/problem/10809
S = input()
word = [ord(x) for x in S]
for i in range(97, 123):
    if i in word:
        print(word.index(i), end=' ')
    else:
        print("-1", end=' ')
