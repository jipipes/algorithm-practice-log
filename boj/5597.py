import sys
submit = [int(sys.stdin.readline().strip()) for _ in range(28)]
for i in range(1, 31):
    if i not in submit:
        print(i)
