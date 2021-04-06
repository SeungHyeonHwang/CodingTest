
# Day    : 4/4
# Start  : 12:05 
# Finish : 
# Level  : 


from itertools import product
import copy
N=int(input())
my_maps=[list(map(int,input().split())) for _ in range(N)]
order=list(product([0,1,2,3], repeat=5))

def play(w):
    if w==0:
        for i in range(N):
            count=0
            for j in range(N-1):
                if maps[i][j]==maps[i][j+1]:                
                    maps[i][j]=maps[i][j]*2
                    maps[i][j+1]=0
            count=0
            for j in range(N):
                if maps[i][j]!=0:
                    if j!=count:
                        maps[i][count]=maps[i][j]
                        maps[i][j]=0
                        count+=1
                    else:
                        count+=1
    elif w==1:
        for i in range(N):
            count=0
            for j in range(N-1,0,-1):
                if maps[i][j]==maps[i][j-1]:
                    maps[i][j]=maps[i][j]*2
                    maps[i][j-1]=0
            count=0
            for j in range(N-1,-1,-1):
                if maps[i][j]!=N-1-count:
                    if j!=N-1-count:
                        maps[i][N-1-count]=maps[i][j]
                        maps[i][j]=0
                        count+=1
                    else:
                        count+=1

    elif w==2:
        for j in range(N):
            count=0
            for i in range(N-1):
                if maps[i][j]==maps[i+1][j]:                
                    maps[i][j]=maps[i][j]*2
                    maps[i+1][j]=0
                    count+=1
            count=0
            for i in range(N):
                if maps[i][j]!=0:
                    if i!=count:
                        maps[count][j]=maps[i][j]
                        maps[i][j]=0
                        count+=1
                    else:
                        count+=1


    elif w==3:
        for j in range(N):
            count=0
            for i in range(N-1,0,-1):
                if maps[i][j]==maps[i-1][j]:                
                    maps[i][j]=maps[i][j]*2
                    maps[i-1][j]=0
            count=0
            for i in range(N-1,-1,-1):
                if maps[i][j]!=0:
                    if i!=N-1-count:
                        maps[N-1-count][j]=maps[i][j]
                        maps[i][j]=0
                        count+=1
                    else:
                        count+=1



result=0
for ors in order:
	maps=copy.deepcopy(my_maps)
	for k in ors:
		play(k)
	for i in range(N):
		print(maps[i])
	print()
	for i in range(N):
		for j in range(N):
			if result<maps[i][j]:
				result=maps[i][j]

print(result)
