import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    for j in range(n, n-i):
        print(" ", end=" ")
    for k in range(1, i):
        print("*", end=" ")
    print()