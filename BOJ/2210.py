"""
숫자판 점프
실2
"""
def dfs(i,j,comb):
    if len(comb) == 6:
        result.add(comb)
        return
    for k in range(4):
        nx,ny = i+dx[k],j+dy[k]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny, comb+str(maps[nx][ny]))
        



dx = [-1,0,1,0]
dy = [0,1,0,-1]

maps = [list(map(int, input().split())) for _ in range(5)]
answer = 0
result = set()
for i in range(5):
    for j in range(5):
        dfs(i,j,str(maps[i][j]))
print(len(result))