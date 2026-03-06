import sys
input = sys.stdin.readline

n = int(input())
for i in range (n // 5, 0, -1):
    remains = n - (5 * i)
    if remains % 3 == 0:
        print(i + remains // 3)
        break
else:
    print(-1)