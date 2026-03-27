import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

print(n*(m%10))
print(n*((m%10)%100))
print(n*(((m%10)%100)%1000))
print(n*m)