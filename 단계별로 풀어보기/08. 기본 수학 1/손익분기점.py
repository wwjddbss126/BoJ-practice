# https://www.acmicpc.net/problem/1712
a, b, c = map(int, input().split())
if(b >= c):
    print(-1)
else:
    print(a//(c-b)+1)
    
    
# 이번 문제는 아래 식을 통해 n을 한 항으로 모는 작업이 필요하다.
# c*n > a+b*n
# c > a/n + b
# c-b > a/n
# (c-b)n > a
# n > a/(c-b)

# 여기서 포인트는 식 내에 n을 포함하지 않고, 비슷하거나 작은 a/(c-b)를 그대로 프린트 한다는 것이다.
# n > a/(c-b)
# print(n) > print(a/(c-b))

# 이 때 print(a/(c-b))를 그대로 쓰면, 마치 '>'가 '='것 같은 결과가 나온다. 
# 즉, n = a/(c-b)와 같아진다.
# 따라서 1을 더해주고, 정수 결과를 위해 int()를 씌워주거나 '/'을 '//'로 바꾼다.
