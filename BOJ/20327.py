
def oper1(sub_num, sub_size):
	for i in range(sub_num):
		for j in range(sub_num):
			for si in range(sub_size//2):
				maps[i*sub_size+si][j*sub_size:(j+1)*sub_size],\
				maps[(i+1)*sub_size-si-1][j*sub_size:(j+1)*sub_size]= \
				maps[(i+1)*sub_size-si-1][j*sub_size:(j+1)*sub_size],\
				maps[i*sub_size+si][j*sub_size:(j+1)*sub_size]

def oper2(sub_num, sub_size):
	for i in range(sub_num):
		for j in range(sub_num):
			for si in range(sub_size):
				for sj in range(sub_size//2):
					maps[i*sub_size+si][j*sub_size+sj],\
					maps[i*sub_size+si][(j+1)*sub_size-sj-1]=\
					maps[i*sub_size+si][(j+1)*sub_size-sj-1],\
					maps[i*sub_size+si][j*sub_size+sj]
def oper3(sub_num, sub_size):
	for i in range(sub_num):
		for j in range(sub_num):
			temp = [[0]*sub_size for _ in range(sub_size)]
			for si in range(sub_size):
				for sj in range(sub_size):
					temp[sj][sub_size-si-1] = maps[i*sub_size+si][j*sub_size+sj]
			for si in range(sub_size):
				for sj in range(sub_size):
					maps[i*sub_size+si][j*sub_size+sj] = temp[si][sj]
def oper4(sub_num, sub_size):
	for i in range(sub_num):
		for j in range(sub_num):
			temp = [[0]*sub_size for _ in range(sub_size)]
			for si in range(sub_size):
				for sj in range(sub_size):
					temp[sub_size-sj-1][si] = maps[i*sub_size+si][j*sub_size+sj]
			for si in range(sub_size):
				for sj in range(sub_size):
					maps[i*sub_size+si][j*sub_size+sj] = temp[si][sj]

def operator(maps,k,l):
	map_size = 2**n
	sub_size = 2**l
	sub_num = map_size//sub_size
	if k==1 : oper1(sub_num, sub_size)
	elif k == 2 : oper2(sub_num, sub_size)
	elif k == 3 : oper3(sub_num, sub_size)
	elif k == 4 : oper4(sub_num, sub_size)
	elif k == 5 : oper1(sub_num//2, sub_size*2)
	for i in range(2**n):
		print(maps[i])
	print()

def solution(n,r):
	for k,l in oper:
		operator(maps,k,l)
	#for i in range(2**n):
	#	print(maps[i])

n,r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(2**n)]
oper = [list(map(int, input().split())) for _ in range(r)]

solution(n,r)