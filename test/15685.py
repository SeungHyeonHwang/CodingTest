

def dragon_curve(curve):
	x,y,d,g = curve[0], curve[1], curve[2], curve[-1]
	curve_list = []
	if not curve_list : 
		maps[y][x]=1
		x,y = x+dx[d],y+dy[d]
		maps[y][x]=1
		curve_list.append(d)
	for i in range(g):
		for j in range(len(curve_list)-1,-1,-1):
			d=(curve_list[j]+1)%4
			x+=dx[d]
			y+=dy[d]
			curve_list.append(d)
			maps[y][x]=1
	return

def solution(n,m):
	answer = 0
	for curve in curves:
		dragon_curve(curve)
	for i in range(m-1):
		for j in range(m-1):
			if maps[i][j] and maps[i+1][j] and maps[i][j+1] and maps[i+1][j+1]:
				answer+=1

	return answer 
m = 101
dx = [1,0,-1,0]
dy = [0,-1,0,1]
n = int(input())
maps = [[0]*m for _ in range(m)]
curves = [list(map(int, input().split())) for _ in range(n)]
print(solution(n,m))