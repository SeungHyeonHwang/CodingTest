





from collections import deque
def solution(n,l,r):
    answer = 0

    while True :
        visited = [[0]*n for _ in range(n)]
        total_nation = []
        q=deque()
        for i in range(n):
            for j in range(n):
                if not visited[i][j] : 
                    q.append((i,j))
                visited[i][j] = 1
                nation = set()
                while q : 
                    x,y = q.popleft()
                    
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0>nx or 0>ny or nx>=n or ny>=n:
                            continue
                        if visited[nx][ny] :
                            continue
                        if l<= abs(population[nx][ny] - population[x][y]) <=r:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                            nation.add((x,y))
                            nation.add((nx,ny))
                if nation : 
                   total_nation.append(nation)
        if len(total_nation) < 1:
            break
        answer+=1
        for each_nation in total_nation :
            result = 0
            for x,y in each_nation : 
                result+=population[x][y]
            result//=len(each_nation)
            for x,y in each_nation:
                population[x][y] = result
                           
    return answer 

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,l,r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
print(solution(n,l,r))
