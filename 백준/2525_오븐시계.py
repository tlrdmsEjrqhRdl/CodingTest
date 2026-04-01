import sys
input = sys.stdin.readline

hour, minutes = map(int, input().split())
time = int(input())

if((minutes + tiem) > 60):
    if(hour == 23):
        print("0", minutes + time - 60)
    print(hour+1, minutes+ time-60)
else:
    print(hour, minutes+time)