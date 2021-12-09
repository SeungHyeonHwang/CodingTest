# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:07:41 2021

@author: USER
"""




def move(start,x,y,dirs):
    global n
    while 0<=x+dx[dirs]<n and 0<=y+dy[dirs]<n:
        x+=dx[dirs]
        y+=dy[dirs]
        if (start[0] == x and start[1] == y) or maps[x][y]!=0:
            return x,y
    return x+dx[dirs],y+dy[dirs] 
    
def play(start, x, y, dirs, result):
    global n,answer

    nx,ny = move(start, x, y, dirs)

    if nx<0 or ny<0 or nx>=n or ny>=n or maps[nx][ny]==5:
        result = result*2+1
        answer = max(answer, result)

    elif (start[0] == nx and start[1] == ny) or maps[nx][ny] == -1:
        answer = max(answer, result)


    elif maps[nx][ny] == 1 :
        if dirs == 2: play(start,nx,ny,3, result+1)
        elif dirs == 1: play(start,nx,ny,0, result+1)
        else : play(start,nx,ny,(dirs+2)%4, result+1)
 
    elif maps[nx][ny] == 2 :
        if dirs == 1: play(start,nx,ny,2, result+1)
        elif dirs == 0: play(start,nx,ny,3, result+1)
        else : play(start,nx,ny,(dirs+2)%4, result+1)
    
    elif maps[nx][ny] == 3 :
        if dirs == 3: play(start,nx,ny,2, result+1)
        elif dirs == 0: play(start,nx,ny,1, result+1)
        else :play(start,nx,ny,(dirs+2)%4, result+1)
        
    elif maps[nx][ny] == 4 :
        if dirs == 2: play(start,nx,ny,1, result+1)
        elif dirs == 3: play(start,nx,ny,0, result+1)
        else : play(start,nx,ny,(dirs+2)%4, result+1)
        
    # 6~10 웜홀    
    elif maps[nx][ny] >=6:
        first = wormhall[maps[nx][ny]-6][0]
        second = wormhall[maps[nx][ny]-6][1]
        if nx == first[0] and ny == first[1] : 
            play(start, second[0], second[1], dirs, result)
        else :
            play(start, first[0], first[1], dirs, result)
        
    return 
   
def solution(n):
    for ball in balls :     
        for dirs in range(4):
            play(ball, ball[0], ball[1], dirs, 0)
    return answer


dx = [-1,0,1,0]
dy = [0,-1,0,1]
T = int(input())
for test_case in range(1,T+1):
    answer = 0
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    wormhall = [[] for _ in range(5)]
    balls = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0 : 
                balls.append([i,j])
            elif 6<=maps[i][j]<=10 : 
                wormhall[maps[i][j]-6].append([i,j])

    print('#%d %d'%(test_case, solution(n)))
