import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
length = list(map(int, input().strip().split()))
length.sort()

left = max(length)
right = sum(length)
minlen = right

while left <= right:
    mid = (left + right) // 2
    blueray = 0
    count = 1

    for i in range(N):
        if blueray + length[i] > mid:
            count += 1
            blueray = length[i]
        else:
            blueray += length[i]

    if count <= M:
        minlen = mid
        right = mid - 1
    else:
        left = mid + 1

print(minlen)      