import sys
input = sys.stdin.readline

ans = -1

n = int(input())
for i in range (n // 5, -1, -1):
    remains = n - (5 * i)
    if remains % 3 == 0:
        ans = i + remains // 3
        break
        
print(ans if ans != -1 else -1)