import sys

input = sys.stdin.readline; #system 모듈을 사용하는 것이 기존 input보다 속도가 빠름
a, b = map(int, input().split()); # 맵핑을 통해서 공백으로 a와 b를 나누기
print(a + b); # a와 b의 합을 출력