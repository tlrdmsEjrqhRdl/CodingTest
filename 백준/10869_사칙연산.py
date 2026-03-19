import sys
input = sys.stdin.readline #system 모듈을 사용하는 것이 기존 input보다 속도가 빠름

a, b = map(int, input().split()) # 맵핑을 통해서 공백으로 a와 b를 나누기
print(a+b) # 더하기
print(a-b) # 빼기
print(a*b) # 곱하기
print(a//b) # 나누기(몫) // 연산자는 기존 / 연산자에서 소숫점을 버리는 연산자
print(a%b) # 나누기(나머지)