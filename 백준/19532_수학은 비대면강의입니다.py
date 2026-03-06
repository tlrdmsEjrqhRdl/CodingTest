import sys

input = sys.stdin.readline #system 모듈을 사용하는 것이 기존 input보다 속도가 빠름

a, b, c, d, e, f = map(int, input().split()); # 맵핑을 통해서 공백으로 a, b, c, d, e, f를 나누기 / 변수와 입력값의 갯수가 정확히 일치해야함

x = (e * c - b * f) // (a * e - b * d) # x의 값을 계산하기 위해서 공식에 대입
y = (a * f - e * d) // (a * e - b * d) # y의 값을 계산하기 위해서 공식에 대입
print(x, y);

# 공식은 다음과 같다.
# ax + by = c
# dx + ey = f
# x = (ec - bf) / (ae - bd)
# y = (af - ed) / (ae - bd) 

# 브루스 포스로 풀기
# import sys
# input = sys.stdin.readline
#
#a, b, c, d, e, f = map(int, input().split())
#for x in range(-999, 1000):
#    for y in range(-999, 1000):
#        if (a * x + b * y == c) and (d * x + e * y == f):
#            print(x, y);
#            exit();