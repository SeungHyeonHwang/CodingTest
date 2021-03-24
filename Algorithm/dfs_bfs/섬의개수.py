# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:58:04 2020

@author: USER
"""


# In[] : https://www.acmicpc.net/problem/4963
# 섬의 개수

from collections import deque


def dfs(land):
    global visited
    q = deque()
    q.append(land)
    
    while q :
        x,y = q.popleft()
        
        for i in range(8) : 
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and maps[nx][ny] == 1 :
                q.append([nx, ny])
                visited[nx][ny] = 1


def solution():
    answer = 0
    global visited
    
    for land in lands :
        if not visited[land[0]][land[1]] :
            dfs(land)
            answer +=1
    return answer



exit_state = True
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
while exit_state :
    w,h = map(int, input().split())
    if w == h == 0 :
        exit_state = False
    else : 
        maps = [list(map(int, input().split())) for _ in range(h)]
        lands = [[i,j] for j in range(w) for i in range(h) if maps[i][j] == 1]
        visited = [[0]*w for _ in range(h)]
        print(solution())


# In[] 