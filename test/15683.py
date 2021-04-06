


cctv = [[[(1,0)],[(0,1)],[(-1,0)],[(0,-1)]],
		[[(-1,0),(1,0)], [(0,1),(0,-1)]],
		[[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
		[[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]],
		[[(0,-1),(-1,0),(0,1),(1,0)]]]

def scan(maps, cctv_pos, cnt):
	global answer
	if cnt == len(cctv_pos):
		result=0
		for i in range(n):
			for j in range(m):
				if not maps[i][j]:
					result+=1
		answer=min(result, answer)
		return
	v,cx,cy = cctv_pos[cnt]
	for i in range(len(cctv[v])): # 종류에 따른 방향 개수
		maps_cp = copy.deepcopy(maps)
		for j in range(len(cctv[v][i])):
			for dx,dy in cctv[v][i]:
				x,y=cx,cy
				while 0<=x+dx<n and 0<=y+dy<m :
					x+=dx
					y+=dy
					if maps_cp[x][y]==6:
						x-=dx
						y-=dy
						break
					if maps_cp[x][y]==0 : 
						maps_cp[x][y]='#' 
		scan(maps_cp, cctv_pos, cnt+1)

answer = int(1e9)
import copy
def solution(n,m):
	global answer 
	scan(maps, cctv_pos, 0)
	return answer

n,m=map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cctv_pos = []
for i in range(n):
	for j in range(m):
		if maps[i][j]!=0 and maps[i][j]!=6:
			cctv_pos.append((maps[i][j]-1,i,j))
print(solution(n,m))