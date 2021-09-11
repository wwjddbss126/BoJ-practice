# https://www.acmicpc.net/problem/2908
# 처음에 짠 코드
a, b = input().split()
a = [int(x) for x in str(a)]
b = [int(x) for x in str(b)]
aa = "".join(map(str, a[::-1]))
bb = "".join(map(str, b[::-1]))
print(aa if aa>bb else bb)

# 더 효율적인 코드!
# print(max(input()[::-1].split()))
