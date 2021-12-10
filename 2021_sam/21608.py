"""
꼭 다시 풀어보기 

"""

n = int(input())
data = [list(map(int, input().split())) for _ in range(n*n)]
maps = [[0]*3]*3
maps[1][1] = data[0][0]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(1,len(data)):
	student = data[i][0]
	love = data[i][1:]

	max_x = 0
	max_y = 0
	max_like = -1
	max_empty = -1
	for j in range(n):
		for k in range(n):
			if maps[j][k] == 0 :
				likecnt = 0
				emptycnt = 0
				for h in range(4):
					nx = dx[h]+j
					ny = dy[h]+k
					if 0<=nx<n and 0<=ny<n:
						# 좋아하는 학생 있으면 
						if maps[nx][ny] in love : 
							likecnt+=1
						if maps[nx][ny] == 0 :
							emptycnt+=1
				# 1,2,3 조건 모두 해당
				# 3은 오름차순 이중 for
				if max_like < likecnt or (max_like==likecnt and max_empty < emptycnt) : 
					max_x = j
					max_y = k
					max_like = likecnt
					max_empty = emptycnt 
	maps[max_x][max_y] = student

likedict = dict()
ans = 0
for j in range(n):
	for k in range(n):
		likecnt = 0
		for h in range(4):
			nx = dx[h]+j
			ny = dy[h]+k
			if 0<=nx<n and 0<=ny<n and maps[nx][ny] in likedict[maps[nx][ny]] : 
				likecnt+=1
		if likecnt == 1 : 
			ans+=1
		elif likecnt == 2 : 
			ans+=10
		elif likecnt == 3 : 
			ans+=100
		else :
			ans+=1000

 




