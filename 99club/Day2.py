#TODO-1: 이미 가지고 있는 랜선, 필요한 랜선의 개수를 각각 K, N으로 입력받는다
#TODO-2: [조건1] 1 <= K <= 10,000, 1 <= N <= 1,000,000 [조건2] K<=N [조건3] 랜선의 길이 <= 2^31 -1 , 센티미터 단위의 정수
#TODO-3: N/K를 했을 때 나온 값(소숫점 이하는 버림)을 p라고 했을때, 입력받은 K개의 랜선 중 길이가 가장 작은 랜선을 p개로 나눌 때 가장 크게 만들 수 있는 길이 확인
#TODO-4: 얻은 값을 전체에 대입해본 후 N개를 만들 수 있는 지 확인
#TODO-5: 아니라면 길이를 줄여가면서 확인, 맞다면 해당 값을 출력 

# def divison(length, lencable):
#     count = sum(cable//length for cable in lencable)
#     return count
# 메모리 사용량과 실행 시간 단축을 위해 함수 호출보다 반복문 내에서 직접 처리 

K, N= map(int, input().split())
lencable = []
for i in range(K):
    lencable.append(int(input()))

start ,end =1, max(lencable)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lencable:
        count += i //mid
    if count >= N:
        start = mid +1
    else:
        end = mid -1
print(end)

# start, end = 1, max(lencable)
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     count = sum(list(cable//mid for cable in lencable))
#     if count >= N:
#         result = mid
#         start = mid +1  
#     else:
#         end = mid -1
# print(result) 