

from itertools import combinations 
import copy
def check(n,maps_cp, comb):
	for pos_num in comb : 
		x,y = pos_num//(n-1), pos_num%(n-1)
		if maps_cp[x][y] or (maps_cp[x][y] and maps_cp[x][y+1]) :
			return False
		maps_cp[x][y] = [1,1]
		maps_cp[x][y+1] = [1,-1]
	return True	

def play(n,m,h):
	answer = int(1e9)
	for i in range(4):
		for comb in combinations(cand_list, i):
			maps_cp = copy.deepcopy(maps)
			if check(n, maps_cp, comb):	
				if comb == (2,11,13):
					for i in range(h):
						print(maps[i])
					print()
				cnt = 0		
				for j in range(n): 
					x,y=0,j
					while x<h : 
						if maps[x][y] : 
							x,y = x+maps[x][y][0], y+maps[x][y][1]
							continue
						x,y = x+1,y
					if j==y:
						cnt+=1
				if cnt == n : 
					answer = min(i, answer)	
	return -1 if answer > 3 else answer

n,m,h = map(int, input().split())
maps = [[[] for _ in range(n)] for _ in range(h)]
pos_list = [i*(n-1)+j for i in range(h) for j in range(n-1)]
init_list = []
for i in range(m):
	x,y = map(int, input().split())
	maps[x-1][y-1] = [1,1]
	maps[x-1][y] = [1,-1]
	init_list.append((x-1)*(n-1)+(y-1))
cand_list = list(set(pos_list)-set(init_list)) 
print(play(n,m,h))
