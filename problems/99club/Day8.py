n = int(input()) # 지도의 크기 n 입력받기
graph = [] 
for i in range(n):
    graph.append(list(map(int, input()))) # 2차원 리스트의 지도 정보 입력 받기

# DFS 이용 특정 노드 방문 후 연결된 모든 노드들 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0 # 지도 밖을 벗어나면 종료
    
    if graph[x][y] == 0:
        return 0
    
    graph[x][y] = 0
    count = 1
        
    count += dfs(x-1, y) # 상
    count += dfs(x+1, y) # 하
    count += dfs(x, y-1) # 좌
    count += dfs(x, y+1) # 우
    
    return count
    
# 모든 노드에 대하여 단지 탐색
complex = 0
house_cnts = []

for i in range(n):
    for j in range(n):
        # 노드 1을 발견하면 새 단지 시작 
        if graph[i][j] == 1:
            house_cnt = dfs(i, j) # 단지 탐색하면서 집 개수 세기
            house_cnts.append(house_cnt) # 집 개수 리스트에 저장
            complex += 1 # 단지 수 +1

# 결과 출력
house_cnts.sort()
print(complex)
for house in house_cnts:
    print(house)