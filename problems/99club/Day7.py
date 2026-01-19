from collections import deque

N, K = map(int, input().split())
next_step = [lambda x: x +1, lambda x: x -1, lambda x: x * 2]

def bfs(N, K):
    visited = set()
    queue = deque([(N, 0)])
    visited.add(N)

    while queue:
        node, steps = queue.popleft()

        if node == K:
            print(steps)
            return
        
        for i in next_step:
            move = i(node)
            if move not in visited and 0 <= move <= 100000:
                queue.append((move, steps + 1))
                visited.add(move)
    
bfs(N, K)