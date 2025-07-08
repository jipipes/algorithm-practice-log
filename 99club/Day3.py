#첫째 줄: 점의 개수, 선분의 개수
#둘째 줄: 점의 좌표 (같은 좌표를 가지는 경우X) -> 일차원 좌표이므로 숫자 하나를 갖음
#셋째 줄~: 각 선분의 시작점과 끝점
#목표: 입력받은 선분마다 위에 입력으로 주어진 점이 몇 개 있는지 출력

#일차원이니까 좌표라는 개념을 생각하기 보다는 수의 나열에서 어디에 위치하는지 범위의 개념으로 보는게 맞는 듯 => 이진탐색?
# => 이 범위에 해당하는 숫자가 있습니까? 찾기

# from bisect import bisect_left, bisect_right

# N, M = map(int, input().split())
# dot = list(map(int, input().split()))
# dot.sort()

# for i in range(M):
#     st, ed = map(int, input().split())

#     st_index = bisect_left(dot, st)
#     ed_index = bisect_right(dot, ed)

#     count = ed_index - st_index
#     print(count)

import sys

N, M = map(int, sys.stdin.readline().split())
dot = list(map(int, sys.stdin.readline().split()))
dot.sort()

def lower(st):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if dot[mid] < st:
            start = mid +1
        else:
            end = mid -1
    return end + 1

def higher(ed):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if dot[mid] > ed:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(M):
    st, ed = map(int, sys.stdin.readline().split())
    print(higher(ed) - lower(st) + 1)