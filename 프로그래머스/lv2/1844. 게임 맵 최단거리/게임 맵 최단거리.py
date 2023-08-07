from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    
    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return -1
    
    visited = [[False] * col for _ in range(row)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        
        if cur_r == row - 1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break
        
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            
            if 0 <= next_r < row and 0 <= next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True
    
    return shortest_path_len

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(x, y):
        n = len(maps)
        m = len(maps[0])
        adventure = deque()
        adventure.append((x, y))
        
        while adventure:
            x, y = adventure.popleft()
            
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                
                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                    continue
                
                if maps[next_x][next_y] == 0:
                    continue
                
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = maps[x][y] + 1
                    adventure.append((next_x, next_y))
        
        return maps[n - 1][m - 1]
    
    answer = bfs(0, 0)
    
    if answer == 1:
        answer = -1
    return answer