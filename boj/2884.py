h, m = map(int, input().split())
if m >= 45:
    print(h, m-45)
else:
    m2 = 45 - m
    if h == 0:
        print(23, 60-m2)
    else:
        print(h-1, 60-m2)