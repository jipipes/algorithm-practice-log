
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

move = [[1,0], [1,1], [0,1], [-1,1]] #우, 우하향 대각선, 하, 좌하향 대각선
result = 0

for i in range(19):
    for j in range(19):
        if board[i][j] !=0:
            color = board[i][j] #바둑돌 색 저장
            
            for dy, dx in move:
                ny, nx, cnt = i + dx, j + dy, 1
                while 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == color:
                    cnt += 1

                    if cnt == 5: #육목 방지
                        if 0 <= i - dy < 19 and 0 <= j - dx < 19 and board[i - dy][j - dx] == color:
                            break
                        if 0 <= ny + dy < 19 and 0 <= nx + dx < 19 and board[ny + dy][nx + dx] == color:
                            break

                        if color == 1:
                            result = 1
                        if color == 2:
                            result = 2
                        y, x = i, j
                    ny += dy
                    nx += dx


if result > 0:
    print(result)
    print(y + 1, x + 1)
else:
    print(0)
