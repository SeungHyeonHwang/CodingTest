
"""
주사위 굴리기
골 5 
주사위를 인덱스에 따라 관리하는 것이 핵심
반복하는 회전을 관리하기 위해 temp를 이용

"""

n,m,x,y,k = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
# changeDir 동,서,북,남 인덱스
changeDir =((3,1,0,5,4,2), 
			(2,1,5,0,4,3),
			(4,0,2,3,5,1),
			(1,5,2,3,0,4))
dice = [0]*6

def play(n,m,x,y,k):
	for move in moves:
		x+=dx[move-1]
		y+=dy[move-1]
		if x<0 or y<0 or x>=n or y>=m :
			x-=dx[move-1]
			y-=dy[move-1]
			continue
		temp = dice[:]
		# 회전 
		for i in range(6):
			dice[i]=temp[changeDir[move-1][i]]

		# 지도가 0이 아니면 
		if not maps[x][y] : 
			maps[x][y] = dice[-1]
		else : 
			dice[-1] = maps[x][y]
			maps[x][y]=0
		# 바닥 출력
		print(dice[0])

play(n,m,x,y,k)