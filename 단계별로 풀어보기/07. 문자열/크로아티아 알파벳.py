# https://www.acmicpc.net/problem/2941
word = input()
abc = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in abc:
    if i in word:
        word = word.replace(i, ' ')
print(len(word))
