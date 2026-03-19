import sys

input = sys.stdin.readline #system 모듈을 사용하는 것이 기존 input보다 속도가 빠름

n, m = map(int, input().split()) # 맵핑을 통해서 공백으로 n과 m을 나누기
cards = list(map(int, input().split())) # 아랫줄의 카드들을 배열을 통해서 cards 배열에 저장마찬가지로 맵핑을 통해 공백구분

max_sum = 0 # max_sum을 선언 최소값인 0으로 시작

for i in range(n - 2): # 어차피 카드를 j 랑 k가 보장되어야 하니 n-2 만큼 for문 반복
    for j in range(i + 1, n - 1): # j의 인덱스 번호는 항상 i의 앞에 있어야 하니 j = i + 1이고 j의 앞에는 k가 있어야 함으로 n-1만큼 for문 반복
        for k in range(j + 1, n): # k의 인덱스 번호는 항상 j의 앞에 있어야 하니 k = j + 1이고 n의 끝까지 순환하므로 n만큼 for문 반복
            s = cards[i] + cards[j] + cards[k] # 임의로 s라는 변수를 만들어서 세 카드의 합을 계산
            if s <= m and s > max_sum: # 계산한 합이 m보다 작고 기존의 max_sum 보다 큰지 확인
                max_sum = s # 만약 기존의 max_sum 보다 큰 s라면 max_sum을 교체

print(max_sum) # 이렇게 for문을 돌려서 나온 max_sum의 값을 반환