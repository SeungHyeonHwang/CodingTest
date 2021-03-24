# In[] : https://www.acmicpc.net/problem/16236
# 아기 상어 
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

from collections import deque
def bfs() :
    global time
    q = deque()

    q.append([baby_shark[0], baby_shark[1]])
    # 한번 경로를 찾을 때마다 초기화
    visited = [[0]*n for _ in range(n)]
    visited[baby_shark[0]][baby_shark[1]] = 1
    
    fishes = []
    graph[baby_shark[0]][baby_shark[1]] = 0
    while q :
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나면 안됨
            if nx <= -1 or nx >= n or ny <= -1 or ny >=n :
                continue 
            # 물고기가 상어 사이즈보다 크면 안됨
            if graph[nx][ny] > baby_shark[2] : 
                continue
            if visited[nx][ny] != 0:
                continue
            
            # 먹을 물고기가 있으면
            if 0 < graph[nx][ny] < baby_shark[2] :
                # 우선순위를 위해 list에 담음
                visited[nx][ny] = visited[x][y] + 1
                fishes.append([nx, ny, visited[nx][ny]])
            else : 
                q.append([nx,ny])
                visited[nx][ny] += visited[x][y] + 1
                
    if fishes :         
        
        fish = sorted(fishes, key=lambda x:(x[2], x[0], x[1]))[0]
        baby_shark[0] = fish[0]
        baby_shark[1] = fish[1]
        time += fish[2]-1   
        
        baby_shark[3] +=1
        graph[fish[0]][fish[1]] = 0
        
        if baby_shark[2] == baby_shark[3] :
            baby_shark[3] = 0 # count초기화
            baby_shark[2] +=1 # 사이즈 증가
        return True
       
    return False
    
    
for i in range(n) : 
    for j in range(n) :
        if graph[i][j] == 9:
            x = i
            y = j
time = 0
size = 2
count = 0 
time = 0
baby_shark = [x, y, size, count]    

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while bfs() : 
    pass
print(time)



