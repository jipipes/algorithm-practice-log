def BinarySearch(st, en, med1, num):
    while st <= en:
        mid = (st+en) // 2

        if med1[mid] == num:
            return 1
        elif med1[mid] < num:
            st = mid+1
        else:
            en = mid-1
    return 0

t = int(input())
for i in range(t):
    f = int(input())
    med1 = list(map(int, input().split()))
    med1.sort()
    s = int(input())
    med2 = list(map(int, input().split()))
    for num in med2:
        print(BinarySearch(0,f-1, med1, num))