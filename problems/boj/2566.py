A = [list(map(int, input().split())) for _ in range(9)]
m = max(max(row) for row in A)
max_row, max_col = 0, 0

for i in range(9):
    if m in A[i]:
        max_row = i
        max_col = A[i].index(m)
        break

print(m)
print(max_row+1, max_col+1)
