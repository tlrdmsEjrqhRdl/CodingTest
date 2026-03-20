import sys
input = sys.stdin.readline

a, b = map(input().split())
if(a < b):
    print("<")
elif(a > b):
    print(">")
elif(a == b):
    print("==")